# SOP 2: Punch list, then fix CV

Goal: find every difference between the CV job and the drawings, publish the punch list, get the CV-side fixes made in a copy of the job, and re-check them, so Guillermo only has to review and release.

On Bodie punch lists "Mo" is Guillermo. Punch lists are made here or in the Bodie Checker project. Either way, the fix stage runs through the punch folder on aiworkstation (CV-Agent\workflows\PUNCH-LIST.md, Guillermo's standing workflow since 11/24/26).

## Inputs
- Company, job, room(s).
- The drawings: a Bodie shop drawing set (Client Copy PDF) or architectural drawings.
- CV output: assembly sheet for each cabinet, Toe Kick Assembly Sheet, Door & Drawer List, Drawer & Rollout List, CNC Cut List, Panel Stock, Solid Stock, Manifest, Material Summary. If Guillermo gives the job instead, open a sandbox copy and read these from CV.
- Where Bodie files live (SharePoint, bodiecarpentry.sharepoint.com/sites/Company, Shared Documents/1. PROJECTS/<Job>/): shop drawings in 2. DRAFT-ENGINEER/1. Shop Drawings, CV output in 7. CNC/<ROOM>. Use the Microsoft 365 connector to find and read them.

## Part 1: build the punch list
- **Bodie shop drawings:** follow reference/bodie-cv-check-context.md exactly: matching (section 5), CV math (7), Bodie standard (8), finding classes (4), output (15, Appendix B template, Appendix C crop helper). That file is an 11/03 snapshot; Jordan's core/RULINGS.md in the engine repo overrides it. If the PDF's rulings version differs from the file's, say so at the top. A hand-drafted set (no engine version in the PDF, like the Mud Room and Laundry sets) hasn't passed the engine's drafting checks, so its drafting errors go in Shop drawing fixes.
- **What a correct result looks like:** reference/bodie-cv-check/monterey-kitchen-punch-list-answer-key.json (50 cards). The Monterey Mud Room (11/23) and Laundry (11/24) lists are more examples.
- **Architectural drawings** (no Bodie shop drawing yet): the architect's drawings decide what exists (cabinets, sizes, counts, finishes). The company standard decides how it's built. When a size is scaled off the drawing instead of dimensioned, say "scaled" on the card. *Proposed, confirm with Guillermo:* never fix CV from a scaled size without his OK. Cabinet Tech / AWI rules get written here when that work starts.
- Say which pages and CV sheets were covered and which couldn't be read.
- Publish the punch list artifact.

## Part 2: get the CV fixes made
For CV-side items only, this replaces "report only" in section 1 of the Bodie check context. The shop drawing and other files are still never edited.

### 1. Give every card an owner (the punch folder's owners)
| Card | Owner | What happens |
|---|---|---|
| "Mo:" fix with an exact target, not HOLD | `cv-agent` | fixed this round |
| HOLD, "Jordan:", "Jordan / Mo:", design calls | `jordan` | not touched; questions can go to Jordan as a PDF (example: "Monterey Laundry - Questions for Jordan - 11.24.26.pdf") |
| "Drafter:" / shop drawing fixes | `drafter` | not touched |
| Reprints, "BY: IG" approval, S2M, re-exports | `release` | Guillermo does these when he releases |
| "Mo:" card that asks a question ("confirm", "or", "match other") | ask Guillermo first | becomes `cv-agent` or `jordan` once he answers |
| Needs a template, CV setting, schedule, UCS or construction change | ask Guillermo first | never a `cv-agent` item without his OK |

Read each fix line against the drawing and the CV job, not literally. On 11/04 a fix said "backs 35 1/2\"" and the right value was 34 1/2\", the leg height. When a number doesn't fit the context, ask.

### 2. Write the round into the punch folder
In CV-Agent\punchlists\<job-room>\ (follow punchlists\monterey-circle-laundry\ as the example):
- **TASK.md**, in plain words:
  - Approval line ("Guillermo approved this run: copy the job into the sandbox...").
  - The customer job path (read only, never opened), the sandbox copy name, and the results folder.
  - One section per `cv-agent` item, in the order to do them, using CV assembly numbers, with every change written as before > after (e.g. "#8: box depth 36 > 35 3/4").
  - What must NOT change, and any neighbouring sizes to report before and after.
  - A closing "Not yours this round" list.
- **punchlist.json**: every item with id, owner, status (todo, hold, waiting, agent_done, verified, reopened), title and CV numbers. Claude owns this file.
- Write the folder name into punchlists\CURRENT.txt.

### 3. The fix is made
- **Default:** Guillermo runs `Start Punch List.cmd`. The local CV Agent (punch profile: sandbox job edits only, no UCS or catalog writes) does the `cv-agent` items and writes results\<ID>.md (DONE or BLOCKED), before/after part lists, and results\_RUN.md.
- **Or, when Guillermo asks:** Claude makes the same fixes itself with computer use, following the same TASK.md and the same rules in workflows\PUNCH-LIST.md, and writes the same results files.

### 4. Check every item
- Read results\_RUN.md and each results\<ID>.md. Check each change against the shop drawing, not just against TASK.md. The report DB is the fastest place to read sizes: Cabinets (W/H/D/Elevation by [Cabinet ID]), Doors and Drawers (Width/Height String by [Cabinet ID]), Parts (cv25_report_parts). Use the printed sheet when the item is about the sheet itself.
- Check the neighbours TASK.md said must not change.
- Set each item to `verified` in punchlist.json, or `reopened` with a new round in TASK.md (same folder, round number +1). Check off verified cards in the punch list artifact with a note ("Verified in <sandbox copy>: <value>, checked on <report/sheet>").

### 5. Hand over
When every `cv-agent` item is verified, tell Guillermo the job is ready to review and release: the sandbox copy's name, the changes, and the items still waiting on Jordan, the drafter or release. On his OK the copy replaces the job (he does it, or tells the agent to).

## Notes
- No tolerance band: 1/16" is a finding.
- Hinge counts and positions are set by CV. Don't make hinge cards unless a hinge breaks a shop drawing convention.
- Face-frame jobs (Monterey Circle) don't use the frameless baseline in section 8.
