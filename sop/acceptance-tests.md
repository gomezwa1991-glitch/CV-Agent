# Acceptance tests: prove each SOP before it's used on a real job

Each test has a known answer, so pass or fail is objective. Run a test the first time an SOP is used, and again after a big change to it. Record the result in the table at the bottom.

## Test 1: UCS (SOP 1)
**1a. Re-check a verified UCS (no catalog change).** Specialty Drawers (UCS 67) is enabled. In UCS Test Bench, open cabinet #2 (its drawer was set to Trash Drawer on 10/12; if the setup has changed, set it again in the sandbox), open the Reports tab, then run cv25_report_parts with cabinet "2" and with_parameters=True.
- Pass: the drawer box parts show COMMENT = TRASH DRAWER, and cabinet #3's drawer (Standard) doesn't.

**1b. Full loop on a harmless new UCS.** Request: "On every Deck, write its size into a _TESTINFO parameter." Expected: one _TESTINFO per Deck reading its DX x DZ (a standard base deck reads about 23.25 wide), and no other part changes.
- Install disabled. Ask Guillermo before enabling it for the test. Rebuild one cabinet, then check with cv25_report_parts with_parameters=True.
- Pass: _TESTINFO matches each Deck's size, the part count is unchanged, and the UCS is disabled again afterwards (or deleted, with his OK).

## Test 2: Punch list (SOP 2)
**2a. Find the issues.** Re-run the Monterey Circle kitchen check blind: shop drawings 9.18.26 plus the CV output as of 11/03 (SharePoint, Monterey Circle job). If the 11/03 CV PDFs have since been overwritten, use the Monterey Mud Room (11/23 run) instead and compare with its published punch list.
- Score against reference/bodie-cv-check/monterey-kitchen-punch-list-answer-key.json (50 cards): a card counts as found when the same root cause is on the new list, whatever the wording.
- Pass: at least 45 of 50 found, every HOLD card found and marked HOLD, and every extra card is a real finding Guillermo agrees with.

**2b. Fix and verify.** In a sandbox copy of UCS Test Bench, pick three cabinets in one room (A, B, C). Note their sizes, then change A's width and B's height by a known amount. Write two exact-target cards ("Mo: make A <original> wide", "Mo: make B <original> tall") and one question card ("Mo: confirm C depth or match A").
- Run it through the punch folder (punchlists\test-bench\TASK.md + punchlist.json, then `Start Punch List.cmd`), so the local agent and Claude's re-check are both tested.
- Pass: both exact cards come back DONE and are verified in the report DB Cabinets table, the question card was put to Guillermo instead of the agent, C didn't change, and the results files say what changed.

## Test 3: Room drafting (SOP 3)
Re-draft the Monterey Circle Entertainment Room (shop drawing 10.10.26, sheets B.41-B.47) in a new sandbox job, using the ORDX import first.
- Expected: the table in claude/cv-room-drafting-process.md ("What was drafted in this room"): back wall 124 7/8, returns 30, height 123 1/2, and 7 objects with their W, H, D, Elev and center-from-left.
- Pass: the Cabinets query matches every W, H, D and Elevation to 1/16". Every position along the wall checks out in the Elevation tab. Numbers are locked and names are in Comment. The standard face layouts are built (3 drawers at 14 1/8", stacked 24" x 55 1/4" doors, shelf counts per the drawing). The hard-elevation list names what's left (counter, cork board frames, back panels, valance and rail, crown, furniture kick).
- Also record which fields the ORDX import set by itself.

### Test 3 for another company (e.g. Cabinet Tech)
The released job is the answer key, so no hand-built table is needed.
1. Copy the company's released test job into its sandbox folder (claude/company-profiles/<company>.md). Open the copy and read its cabinet list for the test room with the Cabinets query in SOP 3, step 5. Save it as the answer key (wall, number, name, W, H, D, Elevation), and note each cabinet's position along the wall from the Elevation tab.
2. Close it. In a new sandbox job, draft the same room from the drawings only, following SOP 3 with the company's standards from its profile. Don't look at the answer key while drafting.
3. Pass: every cabinet in the answer key is there with the same W, H, D and Elevation (to 1/16") and the same position along the wall; numbers and names follow the profile; the hard-elevation list covers what was left. Each difference is either the agent's error (fail) or a change made after the drawings were issued (explain it; Guillermo decides).
4. Record which fields the ORDX import set by itself, and the result in the profile's Readiness table.

## Test 4: Drawings and CAD notes (SOP 4)
On the room from Test 3:
- Part A pass: every sheet's SHEET # reads DP-n, every scene carries the right SCENE LABLE symbol (PLAN / ELEVATION / 3D RENDER), scenes are at 1/2" = 1' (or a listed smaller standard scale), and the sheets are saved in the job.
- Part B pass: the elevation's CAD notes from the 11/10 run (including ADJUST. HEIGHT SHELVING, BACK PANEL, CORK BOARD 40 13/16"(W) x 41"(H), 3/4" APPLIED MOLDING, 1-1/4" FRAME, FIXED HEIGHT SHELF) are on the sheet, point at the right parts and print at 1/8".

## Results
| Date | Test | Pass/Fail | Notes |
|---|---|---|---|
| | | | |
