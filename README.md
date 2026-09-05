# Creative Production Workbench

A small proof of concept for creative operations: turn a brief into structured concepts, preserve constraints, record review, and keep provenance visible.

## Philosophy

Creative AI should increase the number of good decisions, not remove creative direction. The operator owns the brief, brand constraints, accessibility requirements, and final approval.

## What the proof covers

- structured creative brief
- brand and audience constraints
- concept records
- review status
- alt-text requirement
- provenance note for generated or referenced assets
- approval before publication

## Run

```bash
python -m creative.demo
python -m unittest discover -s tests -v
```

Synthetic concepts only. No external publishing is performed.

## Implemented

The repository contains working code, not mockups:

- A `Concept` record that carries a title, a brief, brand and audience constraints, alt text, a provenance note, a status, and an event history (`creative/core.py`).
- An approval gate with metadata requirements: approving a concept without both alt text and provenance raises a `ValueError`, so accessibility and provenance are enforced before anything can move to `approved`.
- A status and event trail: approval flips the concept from `draft` to `approved` and records an `approved` event.
- A runnable demo (`python -m creative.demo`) that builds a concept with brand constraints, alt text, and a provenance note, then approves it.

## Limitations

- The workbench models one concept in memory. There is no asset storage, gallery, publishing pipeline, or external system.
- Approval is a state change only. The code does not publish anywhere and does not enforce a separate human reviewer role.
- Alt text and provenance are free-text strings. Nothing validates their quality, and there is no image analysis or generation in this proof of concept.
- Concepts and events disappear when the process exits; there is no database.
- All concepts are synthetic.

## Tests

The standard-library `unittest` suite lives in `tests/test_core.py` and verifies that approval raises a `ValueError` when a concept is missing the required alt text and provenance metadata.

Run it locally with `python -m unittest discover -s tests -v`. GitHub Actions runs the same command on every push to `main` and every pull request into `main` (see `.github/workflows/tests.yml`), with read-only token permissions and no credentials stored in the workflow.
