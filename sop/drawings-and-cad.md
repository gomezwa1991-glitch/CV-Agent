# SOP 4: Drawings and CAD notes (after Guillermo approves the rooms)

Goal: plan and elevation sheets saved in the CV job, ready for Guillermo to edit and print, with the shop drawing's CAD notes already on them.

## Part A: plan and elevation sheets

### Bodie (CV 2025)
1. Work in the approved job (the sandbox copy, or the original if Guillermo says so).
2. Check this PC's Preferences > User > Comment = `{draw.no}` (start screen, job closed). Without it, SHEET # prints "DP-". See claude/cv-marker-fill.md.
3. Reports > Plan & Elevation Sheet > To Drawing, using templates "Bodie Floor Plan 2026" and "Bodie Wall Elevations 2026". Don't change the templates without asking (backups: "... - BACKUP 10-27-26").
4. For each scene: right-click > Scale > the largest standard architectural scale that fits the sheet with its label.
5. Layout to match the finished reference print (claude/handoff-template-scene-labels.md): plan sheet = PLAN scene left, 3D scene right; elevation sheet = ELEVATION scene left, cabinet table right.
6. Scene labels: plan scenes must say PLAN and elevations ELEVATION, each with a standard SCALE line and its own ID. **Open:** where CV sets the generated scene label (next step in handoff-template-scene-labels.md). Until that's found, fix labels on the sheet by hand and list them.
7. Save the job.
8. Check: open every sheet. SHEET # reads DP-n, the label word and ID are right, the scale is standard, nothing hangs off the sheet.

Report-made scenes are static. After a design change, re-run the report for that room.

### Cabinet Tech (later)
Scene templates Plan Auto / Elevation Auto, then a standard scale per scene. See claude/handoff-cabinet-tech-plan-elevation-automation.md.

## Part B: CAD notes from the shop drawing

1. Read the shop drawing elevations and list each note: text, the cabinet and part it points at, the view, and the arrow point measured from the cabinet's lower-left corner.
2. Put the notes in CV by the first route that works on this PC:
   - **a. UCS route ("hard code", preferred).** A "Cabinet Notes" UCS reads the note text from cabinet attributes and draws cvLeader / cvText on the cabinet with AddCAD (RemoveCAD first, `_CADSHOW` = 2 so it shows in room elevations and on drawings). The notes then move with the cabinet. Needs CV 2025.4+ and the x2D CAD multiplier. See claude/cvguy-playlist-findings.md and claude/draft-ucs/auto-elevation-dims.md, which uses the same objects.
   - **b. File route.** Write the notes into a DXF outside CV and import it into the drawing scene at the scene's scale.
   - **c. Computer use (works today).** CAD F7 > Leaders in the room Elevation tab, steps in claude/cv-room-drafting-process.md ("CAD notes").
3. Text size: printed text is 1/8". In the room, Fixed Scale = No and Height = 1/8" x scale factor (3/4" = 1' gives 2"). On static sheets, window-select the texts, then Fixed Scale = Yes and Height = 0.125. See claude/cad-text-fixed-scale.md.
4. Check: open the sheet. Every note is there, points at the right part, prints 1/8", and doesn't cross a dimension.

## Tests to run first (in this order)
1. **x2D CAD on aiworkstation:** in the Test Bench, does `_cvSystem.CreateObject('cvText')` return an object? UCS 73 failed with "CAD objects not available", so it may be missing. Yes = build route a (and run the Auto Elevation Dims draft). No = check the CV build and the x2D license with Guillermo.
2. **DXF into a drawing scene:** does CV's Drawings tab import a DXF/DWG onto a sheet and keep its scale? Decides route b.
3. **Scene label symbol:** where the generated label is set, so PLAN / ELEVATION, the ID and the scale come out right.
