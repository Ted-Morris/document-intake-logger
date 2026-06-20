# Decision Log — Document Intake Logger (DIL)

> Canonical, git-tracked source of truth for this project's decisions.
> Anytype mirrors this file; if they ever disagree, this file wins.
> This file was backfilled on 2026-06-20 from the Anytype record, which had
> been carrying the full history in the absence of this file. All dates below
> reflect when each decision was actually made, not when this file was created.

---

## 2026-06-20 — DIL v0.1 formally closed

**Status:** CLOSED

All five Definition of Done lines confirmed green:
- End-to-end run on real input
- Documented for a stranger
- Clean/testable commit history
- Pushed to GitHub, origin/main synced
- Green tests, no loose ends

**Commit:** `9d48623`
**Working tree:** clean

This closes the hard gate that was blocking all Pokémon TCG AI Battle Challenge
coding work. Pokémon implementation work is now unblocked (Phase 2 — Engine &
Environment — is the live front as of this date).

**Resolved hypothesis:** the previously flagged possible gap ("empty-file
behavior observed manually but may not yet be automatically tested") is
resolved as part of this closure. All DoD lines are green, which would not be
true if that gap were still open.

---

## 2026-06-19 (or earlier) — Empty-file validation added

**Completed:**
- Added automated empty-file validation.
- New `tests/validate_empty_file.py` asserts empty input → 0/0/0 counts,
  exit 0, via subprocess + stdout check.
- Wired as 7th step in `run_all_validations.py` (`vrun` now reports 7 steps,
  all PASS).
- Committed `data/empty_document.txt` fixture.
- README synced: fixed `outputs/` path typo, updated structure tree, added
  LICENSE, documented JSON-reset behavior.
- Removed stray empty `test/` directory.
- **Validation coverage:** 7 steps — happy path (sample + alternate doc
  summaries + JSON), document-path selection, missing-file (exit 1),
  empty-file (exit 0).

**Decisions:**
1. Empty file = valid input, exit 0 — correct v0 contract, pins
   observed/accepted behavior.
2. Empty-as-error deferred to v0.1: a silently-accepted empty file logs a
   zero-content record that can mask a broken upload, defeating the logger's
   purpose. Implement in `read_document.py` + test, after v0.
3. `outputs/intake_summary.json` stays committed at default values
   (4/35/197); it's the fixture `validate_intake_summary.py` checks, and
   `vrun`'s restore-default step leaves it clean after a full run.

**Observation — empty document behavior (recorded before the fix above):**

Tested:
```
python .\src\read_document.py .\data\empty_document.txt
```

Result:
- Program printed a normal document summary
- File name: `empty_document.txt`
- Line count: `0`
- Word count: `0`
- Character count: `0`
- Exit code: `0`

Current behavior at the time: an empty input file is accepted as valid input.

Learning note: before adding validation, current behavior was confirmed
first. This avoids guessing and helps decide whether the next test should
protect existing behavior or define new expected behavior.

---

## Earlier — Missing-file validation added

**Completed:** Added `tests/validate_missing_file_error.py` to verify that
`src/read_document.py` handles a missing input file correctly.

**Confirmed:**
- Uses `sys.executable`
- Runs from `PROJECT_ROOT`
- Captures output
- Expects exit code 1
- Confirms exact error output
- Added to `run_all_validations.py`
- `vrun` now passes 6 validation steps

**Commit:** `9d48623` (validation loop complete)
**State:** Closed

---

## Backlog — explicitly deferred (not started)

- v0.1 empty-as-error change (see 2026-06-19 Decision #2 above) — only if
  DIL is revisited.

## Do Not Add Yet
- Streamlit
- Financial Research Automation
- SIPS
- VA document automation
- Divorce document automation

---

## Project reference

- **Parent Track:** AI Automation Portfolio Track
- **Purpose:** Beginner Python portfolio project showing document intake,
  validation, GitHub workflow, and automated testing.
- **Project Folder:** `C:\ai-engineering-learning\document-intake-logger`
- **GitHub:** https://github.com/Ted-Morris/document-intake-logger.git
- **Next active project (per "one active path at a time" rule):** Pokémon
  TCG AI Battle Challenge
