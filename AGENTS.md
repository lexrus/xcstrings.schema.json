# Repository Guidelines

## Project Structure & Module Organization
- `examples/` contains reference `.xcstrings` catalogs used to validate schema coverage.
- `xcstrings.schema.json` is the canonical Draft 7 schema for `.xcstrings` files.
- `validate_examples.py` loads the schema and checks every catalog in `examples/`.
- `README.md` introduces the project; `LICENSE` contains the MIT license terms.

## Build, Test, and Development Commands
- `python3 validate_examples.py` validates all bundled catalogs; run after schema edits.
- `python3 validate_examples.py path/to/catalog.xcstrings` validates a single external catalog.
- `python3 -m json.tool <file>` pretty-prints JSON for easier diffing and review.

## Coding Style & Naming Conventions
- Prefer Python 3.9+ features (e.g., type annotations) and follow PEP 8 spacing/indentation.
- Keep filenames lowercase with underscores (e.g., `validate_examples.py`).
- Maintain schema keys in `camelCase` to match Apple's catalog format.

## Testing Guidelines
- Use the `jsonschema` Draft 7 validator via `validate_examples.py`; ensure all examples pass before merging.
- Add new sample catalogs covering edge cases whenever schema changes extend coverage.
- When reproducing bugs, commit failing examples first, then update the schema and script until they pass.

## Commit & Pull Request Guidelines
- Follow concise, imperative commit messages (e.g., `Add substitution variations to schema`).
- Pull requests should describe schema changes, new examples, and validation results.
- Link related issues and include command output snippets if validation fails or requires explanation.

## Security & Configuration Tips
- Avoid committing proprietary catalogs; scrub sensitive strings before adding examples.
- Run `python3 -m pip install jsonschema` in a virtual environment to keep dependencies isolated.
