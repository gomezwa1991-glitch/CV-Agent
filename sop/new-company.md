# SOP 0: Set up and test a company

Use this before the agent does real work for a company's catalog (first Bodie Carpentry, next Cabinet Tech). The four job SOPs stay the same for every company; what changes per company lives in its profile.

## 1. Fill the company profile
Copy claude/company-profiles/_template.md to claude/company-profiles/<company>.md and fill it with Guillermo. Every field is either filled, or marked TBD with who will answer it. The profile names the PC, CV version, catalog, license, how the agent reaches the PC, where jobs live, the sandbox folder, the standards, the drawing style, who makes design calls, and what may be installed.

## 2. Access check (read only, nothing changed)
On the company's PC, prove each of these and write the result in the profile's "Access check" table:
1. The agent can see the screen and drive CV (computer use), with the CV version named in the profile.
2. CV opens with the right license (the company's license name shows in CV's About or License Wizard).
3. The catalog can be read: either a read-only database tool (like cv25_*) or, without one, the UCS Manager and Part Manager on screen.
4. The report DB (or the Reports tab) shows the open job's name.
5. The sandbox folder exists, and a test job can be Save As'd into it.
6. Where scripts can run: a build helper like _dev\inbox, or none (then UI only).

## 3. Pick the test job
A finished, released job with a known answer: the drawings it was built from (architectural or shop drawings), the CV job as released, and the approved shop drawings or submittal. Copy the CV job into the company's sandbox folder. The original is never opened.

## 4. Run the acceptance tests
Run claude/sop/acceptance-tests.md against the company's test job, in this order: Test 1 (UCS, read-only part first), Test 3 (re-draft one room of the test job), Test 4 (drawings for that room), Test 2 (punch list: compare the drawings with the released CV job; the released job's own corrections are the known answer). Use the company's standards from the profile wherever an SOP says "company standard".

## 5. Record and decide
Record each result in the profile's "Readiness" table, with the date and what failed. A job type is ready for that company when its test passes. Until then, the agent may do that job only with Guillermo watching.

## Rules
- Each company's catalog is treated as production until the profile says otherwise. The stop points in the project instructions apply in full.
- Nothing is installed on a company PC without Guillermo's OK (stop rule). The profile records what was approved.
- One company's standards never fill another company's gaps. If the profile is silent, ask.
