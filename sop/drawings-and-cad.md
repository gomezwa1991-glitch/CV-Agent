# SOP 4: Drawings and CAD notes (after Guillermo approves the rooms)

Goal: plan and elevation sheets saved in the CV job, ready for Guillermo to edit and print, with the shop drawing's CAD notes already on them.

## Part A: plan and elevation sheets

### Bodie (CV 2025)
Follows CV-Agent\workflows\PLAN-ELEVATION-SHEETS.md (checked in the Test Bench on 10/28).
1. Work in the approved job (the sandbox copy, or the original if Guillermo says so).
2. Check this PC's Preferences > User tab > Comment = `{draw.no}` (start screen, job closed; this is the user preference, not a cabinet's Comment field). Without it, SHEET # prints "DP-". See claude/cv-marker-fill.md.
3. Reports > Plan & Elevation Sheet > To Drawing. The templates are named **"Brodie Floor Plan 2026"** and **"Brodie Wall Elevations 2026"** in CV (spelled with an R; the "Bodie ... - BACKUP 10-27-26" entries are the backups). Don't rename or change them without asking.
4. For each scene (about 8 clicks):
   - Right-click the scene > Properties > Scale tab > **1/2" = 1'** > OK. If a scene doesn't fit at 1/2", use the next standard scale down and list it.
   - With the scene selected: CAD (F7) > Insert > Bodie Standard Symbol > double-click the matching label: SCENE LABLE (PLAN), (ELEVATION), (3D RENDER) or (SEC.). A single click or a drag does nothing.
   - Click below the scene's lower-left corner to place it, then Esc, then Return.
   - Switch to another sheet and back, so the title block's {draw.scale} refreshes.
5. Layout to match the finished reference print (claude/handoff-template-scene-labels.md): plan sheet = PLAN scene left, 3D scene right; elevation sheet = ELEVATION scene left, cabinet table right.
6. Save the job.
7. Check: open every sheet. SHEET # reads DP-n, each scene has the right label (PLAN / ELEVATION / 3D RENDER / SEC.), the scale is standard, nothing hangs off the sheet.

Known limits (10/28): the label bubble and underline are model units, so they print at their intended size only at 1/2" = 1'. The circle ID is fixed text "1" in every label symbol. Placed labels are static copies. The Floor Plan title block SCALE reads "AS NOTED". Report-made scenes are static, so after a design change, re-run the report for that room.

### Cabinet Tech (later)
Scene templates Plan Auto / Elevation Auto, then a standard scale per scene. See claude/handoff-cabinet-tech-plan-elevation-automation.md.

## Part B: CAD notes from the shop drawing

1. Read the shop drawing elevations and list each note: text, the cabinet and part it points at, the view, and the arrow point measured from the cabinet's lower-left corner.
2. Put the notes in CV by the first route that works:
   - **a. UCS route ("hard code", preferred).** A "Cabinet Notes" UCS reads each note's text and arrow point from cabinet attributes and draws cvLeader / cvText on the cabinet with AddCAD (RemoveCAD first, `_CADSHOW` elevation bit on so it shows in room elevations and on drawings). The notes then move with the cabinet. What's already proven on aiworkstation (CV 2025.4, x2D CAD licensed): AddCAD with cvDimension drew in the Test Bench on 10/19 (UCS 73). UCS 81 has cvText code with `FixedScale = true` (Height = paper size); it was tried in the Test Bench on 11/03, but whether the text drew wasn't recorded. Filling the attributes: through the sidebar, or in the ORDX import if attributes come through (test).
   - **b. File route.** Write the notes into a DXF outside CV and import it into the drawing scene at the scene's scale. Untested.
   - **c. Computer use (works today).** CAD F7 > Leaders in the room Elevation tab, steps in claude/cv-room-drafting-process.md ("CAD notes").
3. Text size: printed text is 1/8".
   - UCS text: FixedScale = true, Height = 0.125 (confirm it holds on live and static scenes).
   - Hand-drawn text: in the room, Fixed Scale = No and Height = 1/8" x scale factor: 3" for the standard 1/2" = 1' sheets (2" at 3/4" = 1'). On static sheets, window-select the texts, then Fixed Scale = Yes and Height = 0.125. See claude/cad-text-fixed-scale.md.
4. Check: open the sheet. Every note is there, points at the right part, prints 1/8", and doesn't cross a dimension.

## Tests to run first (in this order)
1. **cvText and cvLeader from a UCS:** in the Test Bench (enabling needs Guillermo's OK), draw one leader and one text on a cabinet. Pass: both show in the room elevation and on a Plan & Elevation sheet, the text prints 1/8", and a rebuild doesn't duplicate them. This decides route a.
2. **Note attributes through ORDX:** can an imported ORDX set a cabinet attribute (e.g. U_NOTE_1)? If yes, notes go in with the room and no typing is needed.
3. **DXF into a drawing scene:** does CV's Drawings tab import a DXF/DWG onto a sheet and keep its scale? Decides route b.
4. **Per-scene label ID:** a token or symbol that gives each scene its own ID instead of the fixed "1".
