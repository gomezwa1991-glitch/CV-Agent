# SOP 3: Draft rooms in CV from drawings (Bodie first)

Goal: Guillermo opens a job where every wall and cabinet is in place, numbered, named and sized, with the standard door/drawer layout. He only does the hard elevations, then approves. After that, SOP 4 makes the drawings.

Run straight through to step 7, then stop. Click-by-click how-tos and CV quirks are in claude/cv-room-drafting-process.md. Read it before driving CV, and add new quirks to it.

## Inputs
- Company, job, room(s).
- Shop drawing PDF (plan, elevations, sections) or architectural drawings. A DXF of the plan if there is one.
- New job, or rooms added to a job Guillermo started?

## 1. Takeoff (before touching CV)
Build one table per room and post it in the chat:

| Wall | # (drawing tag) | Name | CV catalog item | W | H | D | Elev | From left | Standard face layout | Hard? |
|---|---|---|---|---|---|---|---|---|---|---|

- Read numbers from the PDF's vector data when it has any (PyMuPDF: dimension text and line coordinates). They're exact; reading by eye isn't. A DXF dropped on the CV plan is a visual check; its lines couldn't be selected in the 10/24 run.
- "Standard face layout" = doors, drawers and shelves that CV's normal section tools can build (e.g. "3 drawer 7 / 11 9/16 / 11 9/16", "pair door, 2 adj shelves").
- "Hard?" = Y for anything Guillermo finishes himself, with the reason: angled shelves, custom sections, crown, specialty parts.
- Wall data per room: lengths, height, soffit, openings (windows, doors).
- List every conflict in the drawing (e.g. a section says 20" box, the plan measures 18") and the value used. Where the drawing is silent, use the company's standards from claude/company-profiles/<company>.md (Bodie: reference/bodie-cv-check-context.md section 8) and say so. If the profile is silent too, ask.
- Numbers: use the drawing's cabinet tags, or the numbering rule in the company profile. Bodie engine sets carry no tags until CV numbers exist, so number by wall order (wall 1 left to right, then wall 2...) and put that mapping in the takeoff.

## 2. Job
- New job: create it in CV-Agent\sandbox\ as "<job> - <room> - DRAFT.cvj".
- His started job: Save As a copy into sandbox\ first, unless he says to work in the original.

## 3. Start the room
**a. Order import (preferred; Guillermo has used it).** Write the takeoff as an ORDX (or ORD) file and import it with Room level > Utilities > Import Order.
- Use an ORDX exported by CV from a Bodie room as the pattern, so catalog and item names match the shop's catalog. Import only into the sandbox job.
- Spec: CV help "ORD File Format" (Order Entry v4). It has [Header], [Catalog] and [Cabinet] sections, plus Walls, Windows, Doors and Appliances sections in the extended format. For ORDX, third-party notes (unconfirmed) say it's XML with several rooms per file and cabinets placed by wall, offset along the wall and elevation. The exported sample is the real reference.
- On the first run, record in cv-room-drafting-process.md which fields came through (walls, positions, numbers, Comment) and the export menu path.

**b. Through the screens (fallback, or for what the import didn't set).**
- Walls: Walls F2 > Chained Line. Set Height and Soffit first. Type decimals. +Y is down, and the room side is on the right of travel (draw clockwise so the wall thickness falls outside the room).
- Cabinets: in the Elevation view, drag the catalog item, release, click once to drop, Esc. Size and position from the sidebar: Width first, then re-check every field (the edit right after a Width change is ignored). Set Elevation after Height. Position with Center Position > From Left.

## 4. Number, name and face layout
- **Number:** Properties > Number = the takeoff number, Lock Number = Yes.
- **Name:** the drawing's cabinet name in the cabinet's **Comment** field (Guillermo, 11/24/26, for Bodie; other companies per their profile).
- **Standard face layout:** Section > Section Face for doors and drawers, Section Interior for shelves (Adjustable Shelves + Nominal Spacing).
- Place and size every box, even when its inside is a hard elevation. Leave only the hard parts themselves (angled shelves, custom sections, crown, specialty parts).

## 5. Verify
- Open the Reports tab, check [Job Info].[Job Name], then read the cabinets:
  `SELECT [Room ID],[Wall ID],[Cabinet ID],[Comment],[Cabinet Name],[Width String],[Height String],[Depth String],[Elevation String] FROM Cabinets ORDER BY [Room ID],[Wall ID],[Cabinet ID]` (cv25_query, database "report").
- Every cabinet must match the takeoff: number ([Cabinet ID]; confirm on the first run that it's the CV number), name ([Comment]), W, H, D, Elevation.
- Position along the wall isn't in the report DB. Check it in the Elevation tab against the drawing elevations.
- Fix and re-check until everything matches. Up to 5 rounds per cabinet, then flag it.

## 6. Save
Save the job.

## 7. Hand over, then STOP
- Write the handoff: what was drafted, the hard elevation list (cabinet, what's left, drawing page), the conflicts and the values used.
- Guillermo finishes the hard elevations and approves the rooms. Only then go to SOP 4.

## Other companies
Everything company-specific (PC, CV version, catalog, standards, numbering, sandbox) is in claude/company-profiles/<company>.md. Cabinet Tech: claude/company-profiles/cabinet-tech.md (CV 2026, Claude app on d-6qm2n34).
