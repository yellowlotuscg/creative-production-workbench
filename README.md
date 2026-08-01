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
