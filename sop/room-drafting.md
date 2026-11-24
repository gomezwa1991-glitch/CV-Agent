# SOP 3: Draft rooms in CV from drawings (Bodie first)

Goal: Guillermo opens a job where every wall and cabinet is in place, numbered, named and sized, with the standard door/drawer layout. He only does the hard elevations, then approves. After that, SOP 4 makes the drawings.

The click-by-click how-tos and CV quirks are in claude/cv-room-drafting-process.md. Read it before driving CV, and add new quirks to it.

## Inputs
- Company, job, room(s).
- Shop drawing PDF (plan, elevations, sections) or architectural drawings.
- New job, or rooms added to a job Guillermo started?

## 1. Takeoff (before touching CV)
From the drawing, build one table per room and post it in the chat:

| Wall | # (drawing tag) | Name | CV catalog item | W | H | D | Elev | From left | Standard face layout | Hard? |
|---|---|---|---|---|---|---|---|---|---|---|

- "Standard face layout" = doors, drawers and shelves that CV's normal section tools can build (e.g. "3 drawer 7 / 11 9/16 / 11 9/16", "pair door, 2 adj shelves").
- "Hard?" = Y for anything Guillermo finishes himself, with the reason: angled shelves, custom sections, crown, specialty parts.
- List every conflict in the drawing (e.g. a section says 20" box, the plan measures 18") and the value used. Where the drawing is silent, use the company standard (Bodie: reference/bodie-cv-check-context.md section 8) and say so.
- Wall data per room: lengths, height, soffit, openings.

## 2. Job
- New job: create it in CV-Agent\sandbox\ as "<job> - <room> - DRAFT.cvj".
- His started job: Save As a copy into sandbox\ first, unless he says to work in the original.

## 3. Walls
Walls F2 > Chained Line. Set Height and Soffit first. Type decimals. +Y is down, and the room side is on the right of travel.

## 4. Cabinets
- Place each catalog item from the takeoff (drag, then click on the wall). Size and position from the sidebar: Width first, then re-check every field (the edit right after a Width change is ignored). Set Elevation after Height. Position with Center Position > From Left.
- **Number:** Properties > Number = drawing tag, Lock Number = Yes. If the drawing has no tags, number by wall order (wall 1 left to right, then wall 2...) and put that mapping in the takeoff.
- **Name:** the drawing's cabinet name in the cabinet's name/description field. Record which CV field holds it in cv-room-drafting-process.md on the first run.
- **Standard face layout:** Section > Section Face for doors and drawers, Section Interior for shelves (Adjustable Shelves + Nominal Spacing).
- Skip the "Hard?" items.

## 5. Verify
- Open Reports and read the cabinet list from the report DB (check [Job Info].[Job Name] first). Every cabinet must match the takeoff: number, name, W, H, D.
- Check elevation positions in the Elevation tab against the drawing elevations.
- Fix and re-check until everything matches. Up to 5 rounds per cabinet, then flag it.

## 6. Hand over, then STOP
- Save the job. Write the handoff: what was drafted, the hard elevation list (cabinet, what's left, drawing page), the conflicts and the values used.
- Guillermo finishes the hard elevations and approves the rooms. Only then go to SOP 4.

## Open
- Every field is typed through the UI, so this is slow. A faster import path (cabinet list or XML import) has not been checked yet.
- Cabinet Tech: commercial catalog and AWI standards. Write its defaults here when that work starts.
