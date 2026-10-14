# CV Agent (local)

> Upgrade 2026-10-13: Start CV Local Research.cmd launches the restricted, local-only research profile.
> The original tools remain available. Expanded reference search is available through search_local_reference
> and read_local_reference. The currently loaded model is standard Qwen3.6 35B A3B Q4_K_M (cv-agent);
> the older model/setup notes below describe the previous configuration.


A local AI agent for Cabinet Vision 2025 that runs entirely on this PC:
**Huihui-Qwen3.6-35B-A3B-abliterated** in LM Studio, plus a set of tools (an MCP server called `cv-agent`) that let
it read and write the UCS library, drive the Cabinet Vision window, read CV's parts reports to check results,
and clean up drawings.

## Use it in LM Studio (chat)
1. Open LM Studio and load **Huihui-Qwen3.6-35B-A3B-abliterated** (the "CV Agent" preset sets context and offload).
2. Start a new chat. In the chat's tools (plug icon), make sure **cv-agent** is switched on.
3. Ask for what you need, for example:
   - "Make a UCS that adds a 3/4 MDF kick plate in front of every front toe, then test it."
   - "List my UCS and back them up."
   - "UCS 17 is throwing an error on the test bench, fix it."
   - "Clean up C:\...\Shop Drawings\Kitchen.dwg: merge CV_DIMS into A-ANNO-DIMS, purge, colors ByLayer."
4. LM Studio asks before each tool call. Click **Always allow** for the read-only ones (search_cv_docs,
   verified_ucs, cv_status, cv_screenshot, cv_controls, ucs_list, ucs_get, report_parts, drawing_info,
   list_files, read_file) so it doesn't stop every step.

## Use it from a terminal (no chat window)
`Start CV Agent.cmd` starts LM Studio's server, loads the model and opens an interactive session.
Or one task at a time: `.venv\Scripts\python.exe agent.py "test UCS 20 on the test bench"`.
Every run is logged in `logs\agent-<time>.md`.

## How it tests a UCS
1. Backs up the UCS library (`backups\ucs-<time>\`).
2. Writes the code into the UCS (straight into CV's catalog database).
3. In the sandbox job that's open in CV (`sandbox\UCS Test Bench.cvj`): rebuilds, catches any UCS error
   pop-ups, opens the Reports tab so CV writes its report database, then checks the parts list against what
   the UCS should produce (part names, quantities, sizes, material).
4. Fixes and retests until it passes (up to 5 rounds), then saves the write-up to
   `knowledge\verified-ucs\`.

## Folders
The same `cv-agent` now searches the local UCS library, live UCS mirror (read only), and the
UCS editor, AutoCAD and SketchUp repositories. `sources.json` defines these locations.
Use `list_agent_sources` to inspect availability, `search_cv_docs` to search across sources,
`read_cv_doc` to read a result and `refresh_agent_knowledge` after files change.
Results retain their source paths. This integration does not activate the separate AutoCAD
or SketchUp live servers, fetch remote changes, or index customer jobs, backups or credentials.

| Folder | What's in it |
|---|---|
| `knowledge\` | UCS help reference, verified UCS write-ups, `agent-notes.md` (lessons it learns) |
| `backups\` | UCS library backups, previous versions of every UCS it changed (`ucs-rows\`) |
| `sandbox\` | Test jobs. Customer jobs are only ever copied here, never changed in place |
| `work\` | Cleaned drawings and other outputs |
| `screenshots\`, `logs\` | What it saw and did |

## Safety rails built in
- It refuses to test in, or write files into, the OneDrive project folders. It copies to `sandbox\` or `work\`.
- Every UCS change saves the previous version first (`ucs_restore` undoes it).
- Drawing cleanup always writes a new file. The original is never touched.

## One-time setup (already done unless noted)
- `Grant CV database access.cmd`: gives your Windows login access to CV 2025's catalog DB (run once, CV closed).
- `tools\register.py`: registers the tools with LM Studio (`~\.lmstudio\mcp.json`).
- Settings can be overridden in `config.json` (paths, model name, LM Studio URL).
