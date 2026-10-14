"""CV Agent without the LM Studio chat window: same model, same tools, from a terminal or a scheduled task.

  .venv\\Scripts\\python.exe agent.py                       interactive
  .venv\\Scripts\\python.exe agent.py "test UCS 17 ..."     one task, then exit
  .venv\\Scripts\\python.exe agent.py --file task.txt       task from a file

Needs LM Studio's local server (Developer tab > Start, or `lms server start`) with the model loaded.
Every run is logged to CV-Agent\\logs\\agent-<time>.md.
"""
from __future__ import annotations

import argparse
import asyncio
import base64
import datetime as _dt
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from openai import OpenAI  # noqa: E402
from mcp import Client  # noqa: E402

from cvagent.server import mcp as server  # noqa: E402
from cvagent.config import CFG, LOG_DIR  # noqa: E402

BASE_URL = CFG.get("lmstudio_url", "http://localhost:1234/v1")
MODEL = os.environ.get("CV_AGENT_MODEL") or CFG.get("model", "")
MAX_STEPS = int(CFG.get("max_steps", 40))


def pick_model(api: OpenAI) -> str:
    if MODEL:
        return MODEL
    models = [m.id for m in api.models.list().data if "embed" not in m.id.lower()]
    if not models:
        raise SystemExit("LM Studio has no model available. Load the CV agent model first.")
    for m in models:
        if "qwen3.6" in m.lower() or "abliterated" in m.lower():
            return m
    return models[0]


def to_openai_tools(tools) -> list[dict]:
    out = []
    for t in tools:
        schema = dict(t.input_schema or {"type": "object", "properties": {}})
        schema.pop("title", None)
        out.append({"type": "function", "function": {"name": t.name, "description": (t.description or "")[:1024], "parameters": schema}})
    return out


class Transcript:
    def __init__(self):
        self.path = LOG_DIR / f"agent-{_dt.datetime.now():%Y%m%d-%H%M%S}.md"

    def add(self, title: str, body: str):
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(f"\n### {title}\n{body}\n")


async def run(task: str | None):
    sys.path.insert(0, CFG['local_reference_toolkit'])
    from loop_control import run_bounded_turn
    api = OpenAI(base_url=BASE_URL, api_key="lm-studio", max_retries=0, timeout=180)
    model = pick_model(api)
    system = (HERE / "AGENT_INSTRUCTIONS.md").read_text(encoding="utf-8")
    log = Transcript()
    print(f"CV Agent  model={model}  log={log.path}")
    async with Client(server) as client:
        tools = to_openai_tools((await client.list_tools()).tools)
        messages = [{"role":"system","content":system}]
        async def predict(history, tool_schemas, max_tokens):
            kwargs = dict(model=model,messages=history,temperature=0.2,max_tokens=max_tokens)
            if tool_schemas is not None: kwargs['tools']=tool_schemas
            else: kwargs['tool_choice']='none'
            response=await asyncio.to_thread(api.chat.completions.create,**kwargs)
            return response.model_dump(exclude_none=True)
        async def call(name,args):
            print(f"  -> {name}({json.dumps(args)[:160]})")
            res=await client.call_tool(name,args)
            text="\n".join(p.text for p in res.content if getattr(p,'type','')=='text')
            images=[{'type':'image_url','image_url':{'url':f'data:{p.mime_type};base64,{p.data}'}}
                    for p in res.content if getattr(p,'type','')=='image']
            log.add(f"Tool {name}",text[:6000])
            return {'text':text,'images':images,'is_error':bool(getattr(res,'is_error',False))}
        async def turn(user_text):
            messages.append({'role':'user','content':user_text})
            log.add('User',user_text)
            result=await run_bounded_turn(predict,call,tools,messages,max_rounds=min(MAX_STEPS,12),max_calls=24)
            print('\nAgent: '+result['answer'])
            log.add('Agent',result['answer'])
            log.add('Stop reason',str(result['finish_reason']))
        if task:
            await turn(task)
        else:
            print('Type a request (empty line to quit).')
            while True:
                try: text=input('\nYou: ').strip()
                except (EOFError,KeyboardInterrupt): break
                if not text: break
                await turn(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task", nargs="*", help="task text (omit for interactive)")
    ap.add_argument("--file", help="read the task from a file")
    a = ap.parse_args()
    task = Path(a.file).read_text(encoding="utf-8") if a.file else (" ".join(a.task) or None)
    asyncio.run(run(task))


if __name__ == "__main__":
    main()
