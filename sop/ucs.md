# SOP 1: Write a UCS

Goal: Guillermo describes what he wants in words. The agent delivers a UCS that is installed, tested in CV and written up.

## 1. Pin down the request (ask if anything is missing)
- Company catalog and CV version (Bodie = CV 2025 on aiworkstation).
- What triggers it: the For Each part, a construction method, or a room/cabinet attribute.
- Type: Modify (runs once per matching part, `_this` = that part) or Add (`_this` = the parent).
- Macro Type: JavaScript by default. Classic only when asked.
- **Expected result, written down before any code:** part names, quantity, sizes, material, banding, and which parts must disappear. This list is the test.

## 2. Check what already exists
- claude/ucs-library.md: status of every UCS on aiworkstation.
- claude/verified-ucs/: working examples. Closest starting points: toe-kick-plate (add a part next to a part), toe-kick-wings (place a library part), remake-wall-parts (swap parts by construction), specialty-drawers (per-object choice and tags), oversize-parts (room switch and scribe), rollout-glide-spacers (neighbours, hinges, cabinet frame).
- reference/CV_UCS_Reference.md: UCS help.
- claude/cvguy-playlist-findings.md: CAD from a UCS (cvText, cvLeader, cvDimension, AddCAD).
- Local CV-Agent\library\: shared helpers (lib\), sources (ucs\), builds (dist\). Reuse the helpers.

## 3. Write the code
- Header comment: name, UCS settings (Macro Type, Type, Part, Pre-Build), version and date, and how to test.
- Rules proven in this shop's CV are in the repo's AGENT_INSTRUCTIONS.md under "UCS rules that matter". The ones that bite most:
  - CreateChild: the 2nd argument is the Part Manager name, the 3rd is the cut-list description.
  - ReplacePart doesn't bring a material. Set MATID with SetParameter.
  - Remove a part with QTY = 0. Guard against running twice with a _MARK parameter.
  - No alert(). Write debug text to a _XXINFO parameter or COMMENT instead.
  - Attributes: SetParameter + ModifyParameter(PARSTYLE_ATTRIBUTE). Create one only when HasParameter is false, so the user's value survives.
  - Anything that reshapes a cabinet must be Pre-Build.

## 4. Back up, then install
- Back up the UCS library first (ucs_backup, or a copy into backups\ucs-<time>).
- Install with the local agent's ucs_write / ucs_new_from, or in CV's UCS Manager with computer use.
- CV then asks "Scripts modified externally": answer Yes. "Select UCS to Save" needs an OK click.

## 5. Test in UCS Test Bench (never a customer job)
- Job: C:\Users\gomez\Documents\CV-Agent\sandbox\UCS Test Bench.cvj. Don't save it unless the test setup needs to be kept.
- Rebuild: open the cabinet (double-click it twice in Plan). Closing the UCS Manager doesn't rebuild unchanged cabinets.
- Open the Reports tab so CV writes the report DB. Check [Job Info].[Job Name] = UCS Test Bench before trusting it.
- Compare with the expected list using cv25_report_parts (or the local agent's ucs_test). Parameters such as _XXINFO show with with_parameters=True.
- A part that exists with MATERIAL NOT ASSIGNED means the code works and the schedule is missing a material. Report it; don't change the code.

## 6. Fix and retest
Read the error text and the parts found, fix, reinstall, retest. Up to 5 rounds. Then stop and say exactly what blocks it.

## 7. Write it up
- Passed: claude/verified-ucs/<name>.md with settings, what it does, the test setup and results, findings, and the code. Update the status table in claude/ucs-library.md.
- Not tested in CV: claude/draft-ucs/<name>.md, marked DRAFT at the top.
- Tell Guillermo: UCS id and name, whether it's on or off, what it does, and the test result.

## Cabinet Tech (later)
Different catalog and CV version. Before porting a Bodie UCS, compare it with cv25_compare_ucs and check that its part names and materials exist there.
