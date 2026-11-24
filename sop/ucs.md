# SOP 1: Write a UCS

Goal: Guillermo describes what he wants in words. The agent delivers a UCS that is installed, tested in CV and written up.

**aiworkstation's CV 2025 catalog is production.** A UCS change reaches every job on that catalog, not only the Test Bench. New UCS are installed disabled. Enabling or disabling one, even just for a test, and changing the code of an enabled UCS, need Guillermo's OK.

## 1. Pin down the request (ask if anything is missing)
- Company catalog and CV version (Bodie = CV 2025 on aiworkstation).
- What triggers it: the For Each part or Link To object, a construction method, or a room/cabinet attribute.
- Type: Modify (runs once per matching part, `_this` = that part) or Add (`_this` = the parent).
- Macro Type: JavaScript by default. Classic only when asked.
- **Expected result, written down before any code:** part names, quantity, sizes, material, banding, and which parts must disappear. This list is the test.

## 2. Check what already exists
- **Live list:** cv25_ucs_list (id, name, type, part, enabled, first code line) and cv25_ucs_get for code. It's the source of truth. On 11/24/26 the catalog had 23 rows.
- claude/ucs-library.md: the 10/13 review and the shared helper library. Its status table is out of date; check the live list.
- claude/verified-ucs/: working examples. Closest starting points: toe-kick-plate (add a part next to a part, attributes), toe-kick-wings (place a library part), remake-wall-parts (swap parts by construction), specialty-drawers (per-object choice and tags), oversize-parts (room switch and scribe), rollout-glide-spacers (neighbours, hinges, cabinet frame).
- CAD from a UCS: UCS 73 Auto Elevation Dimensions (cvDimension, tested in CV 10/19: verticals need SetSimple, not SetLinear) and UCS 81 Countertop Plan Numbers (cvText with FixedScale). Background in claude/cvguy-playlist-findings.md.
- reference/CV_UCS_Reference.md: UCS help.
- Local CV-Agent\library\: shared helpers (lib\), sources (ucs\), builds (dist\). Reuse the helpers.

## 3. Write the code
- Header comment: name, UCS settings (Macro Type, Type, Part, Link To, Apply Condition, Pre-Build), version and date, and how to test.
- Rules proven in this shop's CV are in the repo's AGENT_INSTRUCTIONS.md under "UCS rules that matter". The ones that bite most:
  - CreateChild: the 2nd argument is the Part Manager name, the 3rd is the cut-list description.
  - ReplacePart doesn't bring a material. Set MATID with SetParameter.
  - Remove a part with QTY = 0. Guard against running twice with a _MARK parameter.
  - No alert(). Write debug text to a _XXINFO parameter or COMMENT instead.
  - Attributes: SetParameter + ModifyParameter(PARSTYLE_ATTRIBUTE). Create one only when HasParameter is false, so the user's value survives.
  - CAD on a top-level object persists: RemoveCAD(axis) before AddCAD, every run.
  - Anything that reshapes a cabinet must be Pre-Build.

## 4. Back up, then install
- Back up the UCS library first.
- Install routes:
  - **Claude:** a Python script dropped in CV-Agent\_dev\inbox. The first line is `# timeout: N`. It runs in the agent's .venv and uses `cvagent.db.ucs_backup(label)`, `ucs_get(id)` and `ucs_update(id, code=...)`. ucs_update also rewrites CV's compiled copy (Temp\UCSJS\fn<Name>.js); without that, CV's "Scripts modified externally" prompt can restore the old code. The log lands in _dev\outbox. If the CV-Agent folder isn't connected to the chat, request it (device_request_folder_access for C:\Users\gomez\Documents\CV-Agent). If nothing comes back, the helper isn't running: ask Guillermo to double-click _dev\start-build-helper.cmd.
  - **Local agent:** ucs_backup, then ucs_write or ucs_new_from. Run it with only the UCS tools: `.venv\Scripts\python.exe agent.py --profile ucs-build "<task>"` (or `--file <task.md>`).
  - **By hand:** CV's UCS Manager with computer use.
- New UCS: clone a row with the same Type and Macro Type (the local agent's ucs_new_from does this), write the code, and leave it disabled.
- CV then asks "Scripts modified externally": answer Yes. "Select UCS to Save" needs an OK click.

## 5. Test in UCS Test Bench (never a customer job)
- Job: C:\Users\gomez\Documents\CV-Agent\sandbox\UCS Test Bench.cvj. Don't save it unless the test setup needs to be kept.
- Enabling the UCS for the test needs Guillermo's OK (production catalog). Afterwards, set it back to the state he chose.
- Rebuild: open the cabinet (double-click it twice in Plan). Closing the UCS Manager doesn't rebuild unchanged cabinets.
- Open the Reports tab so CV writes the report DB. Check [Job Info].[Job Name] = UCS Test Bench before trusting it.
- Compare with the expected list using cv25_report_parts (or the local agent's ucs_test). with_parameters=True shows _XXINFO values.
- A part that exists with MATERIAL NOT ASSIGNED means the code works and the schedule is missing a material. Report it; don't change the code.

## 6. Fix and retest
Read the error text and the parts found, fix, reinstall, retest. Up to 5 rounds. Then stop and say exactly what blocks it.

## 7. Write it up
- Passed: claude/verified-ucs/<name>.md with settings, what it does, the test setup and results, findings, and the code. Update the status table in claude/ucs-library.md.
- Not tested in CV: claude/draft-ucs/<name>.md, marked DRAFT at the top.
- Tell Guillermo: UCS id and name, whether it's on or off, what it does, and the test result.

## Cabinet Tech (later)
Different catalog and CV version. Before porting a Bodie UCS, compare it with cv25_compare_ucs and check that its part names and materials exist there. On aiworkstation the CV 2026 catalog can't be read until Guillermo runs "Grant CV 2026 read access.cmd" in Documents\CV-Agent once (CV closed).
