# Creative Production Workbench

A small Python proof of concept for creative operations. It keeps one concept in memory: a brief, a list of constraints, alt text, a provenance note, a status, and an event history. Approving the concept requires both alt text and a provenance note.

The operator supplies the brief, the constraints, the accessibility text, and the provenance note. This repository records that decision. It does not generate images, store assets, or publish anything.

## Requirements

Python 3.9 or newer. `Concept` uses `list[str]` at runtime, which needs 3.9+. The only dependency is the standard library. GitHub Actions runs the tests on Python 3.12.

## Setup

Clone the repository and work from its root so `creative` imports as a package:

```bash
git clone https://github.com/yellowlotuscg/creative-production-workbench.git
cd creative-production-workbench
```

There is no install step and no `requirements.txt`.

## Usage

`creative/core.py` defines `Concept` and `approve`. `creative/__init__.py` is empty, so import from `creative.core`.

A `Concept` has these fields:

- `title` (str): short name.
- `brief` (str): what the concept should show or say.
- `constraints` (list of str): brand, audience, or production constraints.
- `alt_text` (str, default `""`): accessibility text for the concept.
- `provenance` (str, default `""`): where the concept, or a referenced asset, came from.
- `status` (str, default `"draft"`): `approve` sets this to `"approved"`.
- `events` (list of str, default empty): `approve` appends `"approved"`.

`approve(concept)` returns the same object after updating it. If `alt_text` or `provenance` is empty, it raises `ValueError` with the message `accessibility and provenance are required` and leaves the concept as it was. Any non-empty string is accepted, including whitespace. Nothing checks whether the text is accurate or useful.

The demo builds one concept and approves it:

```bash
python -m creative.demo
```

That prints:

```text
Concept(title='Local service story', brief='show a before/after workflow', constraints=['gold and navy brand', 'no generated text in image'], alt_text='A service operator reviewing a clear workflow diagram.', provenance='generated concept; final asset review required', status='approved', events=['approved'])
```

The same objects from a script:

```python
from creative.core import Concept, approve

concept = Concept(
    title="Local service story",
    brief="show a before/after workflow",
    constraints=["gold and navy brand", "no generated text in image"],
    alt_text="A service operator reviewing a clear workflow diagram.",
    provenance="generated concept; final asset review required",
)
approve(concept)
```

A concept with the default empty metadata fails approval:

```python
from creative.core import Concept, approve

approve(Concept("x", "y", []))  # ValueError: accessibility and provenance are required
```

## Tests

`tests/test_core.py` uses `unittest`. The one test checks that `approve` raises `ValueError` when alt text and provenance are both left empty.

From the repository root:

```bash
python -m unittest discover -s tests -v
```

`.github/workflows/tests.yml` runs that command on Python 3.12 for pushes to `main` and for pull requests into `main`. The workflow permission is `contents: read`.

## Layout

```text
creative/core.py              Concept and approve
creative/demo.py              Example that builds and approves one concept
creative/__init__.py          Empty package marker
tests/test_core.py            Approval metadata test
.github/workflows/tests.yml   unittest on Python 3.12
LICENSE                       MIT License
```

## Scope

The workbench holds a single concept in process memory. Approval is a status change on that object: `status` becomes `"approved"` and `events` gains `"approved"`. There is no reviewer account, database, file store, gallery, or publishing step. Concepts and events are gone when the process exits. Every example in this repository is synthetic.

## License

Released under the MIT License. Copyright (c) 2026 Matthew Coggins. See [LICENSE](LICENSE).
