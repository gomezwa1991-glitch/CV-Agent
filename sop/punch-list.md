# SOP 2: Punch list, then fix CV

Goal: find every difference between the CV job and the drawings, publish the punch list, then make the CV-side fixes in a copy of the job so Guillermo only has to review and approve.

On Bodie punch lists "Mo" is Guillermo, so the "Mo:" cards are the ones the agent works.

## Inputs
- Company, job, room(s).
- The drawings: a Bodie shop drawing set (Client Copy PDF) or architectural drawings.
- CV output: assembly sheet for each cabinet, Toe Kick Assembly Sheet, Door & Drawer List, Drawer & Rollout List, CNC Cut List, Panel Stock, Solid Stock, Manifest, Material Summary. If Guillermo gives the job instead, open a sandbox copy and read these from CV.
- Where Bodie files live (SharePoint, bodiecarpentry.sharepoint.com/sites/Company, Shared Documents/1. PROJECTS/<Job>/): shop drawings in 2. DRAFT-ENGINEER/1. Shop Drawings, CV output in 7. CNC/<ROOM>. Use the Microsoft 365 connector to find and read them.

## Part 1: build the punch list
- **Bodie shop drawings:** follow reference/bodie-cv-check-context.md exactly: matching (section 5), CV math (7), Bodie standard (8), finding classes (4), output (15, Appendix B template, Appendix C crop helper). That file is an 11/03 snapshot; Jordan's core/RULINGS.md in the engine repo overrides it. If the PDF's rulings version differs from the file's, say so at the top. A hand-drafted set (no engine version in the PDF, like the Mud Room set) hasn't passed the engine's drafting checks, so its drafting errors go in Shop drawing fixes.
- **What a correct result looks like:** reference/bodie-cv-check/monterey-kitchen-punch-list-answer-key.json (50 cards). The Monterey Mud Room list (11/23) is a second example.
- **Architectural drawings** (no Bodie shop drawing yet): the architect's drawings decide what exists (cabinets, sizes, counts, finishes). The company standard decides how it's built. When a size is scaled off the drawing instead of dimensioned, say "scaled" on the card. *Proposed, confirm with Guillermo:* never fix CV from a scaled size without his OK. Cabinet Tech / AWI rules get written here when that work starts.
- Say which pages and CV sheets were covered and which couldn't be read.
- Publish the punch list artifact.

## Part 2: fix CV (Guillermo, 11/24/26: "make the fixes in CV")
For CV-side cards only, this replaces "report only" in section 1 of the Bodie check context. The shop drawing and other files are still never edited.

1. Save As the job into sandbox\: "<job> - <room> - PUNCH FIX MM.DD.YY.cvj". The original stays untouched.
2. Sort the cards before touching CV. Questions don't stop the run; collect them for the hand-over.
   - **Fix:** fix line starts "Mo:", gives an exact target (e.g. "Mo: make both 11 3/4\"", "Mo: set #10 to 26 1/2\""), and isn't HOLD.
   - **Ask Guillermo:** "Mo:" cards that ask a question or offer a choice ("confirm", "or", "match other"). Example: RW-5 "confirm which is right and match other".
   - **Needs a catalog change, ask first:** a template, CV setting or schedule (e.g. ALL-1 reveal setting, the 11 5/8" 3-drawer template, MP-2 template text).
   - **Not the agent's:** HOLD cards, and cards for "Jordan:", "Drafter:" or "Jordan / Mo:" until Jordan answers. Sign-offs ("BY: IG", ALL-3). File tasks such as re-exporting or renaming PDFs in SharePoint (RW-8, SW-10).
3. Read each fix line against the drawing and the CV job, not literally. On 11/04 a fix said "backs 35 1/2\"" and the right value was 34 1/2\", the leg height. When a number doesn't fit the context, ask.
4. One card at a time: make the change to the target size, rebuild, open the Reports tab, then check the value. The report DB is fastest: Cabinets (W/H/D/Elevation by [Cabinet ID]), Doors and Drawers (Width/Height String by [Cabinet ID]), Parts (cv25_report_parts). Use the printed sheet when the card is about the sheet itself. The card counts as fixed only when the value matches the shop drawing.
5. Write in the card's note: "Fixed in <copy name>: <what changed>, checked on <report/sheet>". Check the card off.
6. When all fixable cards are done, re-run the full report set and check the neighbours of every changed cabinet (a width change moves the run).
7. Hand over: the copy's name, the list of changes, and the cards left for Guillermo or Jordan with the reason for each. Guillermo reviews. On his OK the copy replaces the job (he does it, or tells the agent to).

## Notes
- No tolerance band: 1/16" is a finding.
- Hinge counts and positions are set by CV. Don't make hinge cards unless a hinge breaks a shop drawing convention.
- Face-frame jobs (Monterey Circle) don't use the frameless baseline in section 8.
