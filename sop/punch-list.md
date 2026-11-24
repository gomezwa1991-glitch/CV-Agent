# SOP 2: Punch list, then fix CV

Goal: find every difference between the CV job and the drawings, publish the punch list, then make the CV-side fixes in a copy of the job so Guillermo only has to review and approve.

## Inputs
- Company, job, room(s).
- The drawings: a Bodie shop drawing set (Client Copy PDF) or architectural drawings.
- CV output: assembly sheet for each cabinet, Toe Kick Assembly Sheet, Door & Drawer List, Drawer & Rollout List, CNC Cut List, Panel Stock, Solid Stock, Manifest, Material Summary. If Guillermo gives the job instead, open a sandbox copy and produce these from CV.

## Part 1: build the punch list
- **Bodie shop drawings:** follow reference/bodie-cv-check-context.md exactly: matching (section 5), CV math (7), Bodie standard (8), finding classes (4), output (15, Appendix B template, Appendix C crop helper). The answer key reference/bodie-cv-check/monterey-kitchen-punch-list-answer-key.json shows what a correct result looks like.
- **Architectural drawings** (no Bodie shop drawing yet): the architect's drawings decide what exists (cabinets, sizes, counts, finishes). The company standard decides how it's built. When a size is scaled off the drawing instead of dimensioned, say "scaled" on the card. *Proposed, confirm with Guillermo:* never fix CV from a scaled size without his OK. Cabinet Tech / AWI rules get written here when that work starts.
- Say which pages and CV sheets were covered and which couldn't be read.
- Publish the punch list artifact.

## Part 2: fix CV (Guillermo, 11/24/26: "make the fixes in CV")
For CV-side cards only, this replaces "report only" in section 1 of the Bodie check context. The shop drawing and other files are still never edited.
1. Save As the job into sandbox\: "<job> - <room> - PUNCH FIX MM.DD.YY.cvj". The original stays untouched.
2. Fix the cards whose fix line starts "Mo:" (the CV side). Skip HOLD cards and cards for "Jordan:", "Drafter:" or "Jordan / Mo:" until Jordan has answered. List the skipped cards.
3. A fix that needs a template, setting or catalog change (known examples: the 11 5/8" 3-drawer front template, the 3/32" reveal setting) is a catalog change. Ask first.
4. One card at a time: make the change to the exact target size on the fix line, rebuild, re-run the report or sheet the card cites, and compare it with the shop drawing value. The card counts as fixed only when they match.
5. Write in the card's note: "Fixed in <copy name>: <what changed>, checked on <sheet>". Check the card off.
6. When all cards are done, re-run the full report set and check the neighbours of every changed cabinet (a width change moves the run).
7. Hand over: the copy's name, the list of changes, the skipped cards and why. Guillermo reviews. On his OK the copy replaces the job (he does it, or tells the agent to).

## Notes
- No tolerance band: 1/16" is a finding.
- Hinge counts and positions are set by CV. Don't make hinge cards unless a hinge breaks a shop drawing convention.
- Face-frame jobs (Monterey Circle) don't use the frameless baseline in section 8.
