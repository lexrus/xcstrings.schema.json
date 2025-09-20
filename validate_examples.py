from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft7Validator


def main() -> int:
    repo_root = Path(__file__).resolve().parent
    schema_path = repo_root / "xcstrings.schema.json"
    examples_dir = repo_root / "examples"

    if not schema_path.is_file():
        print(f"Schema file not found: {schema_path}", file=sys.stderr)
        return 1
    if not examples_dir.is_dir():
        print(f"Examples directory not found: {examples_dir}", file=sys.stderr)
        return 1

    schema = json.loads(schema_path.read_text())
    validator = Draft7Validator(schema)

    example_files = sorted(examples_dir.glob("*.xcstrings"))
    if not example_files:
        print("No example files found to validate.", file=sys.stderr)
        return 1

    failures: list[tuple[Path, list[str]]] = []

    for example_path in example_files:
        data = json.loads(example_path.read_text())
        errors = sorted(validator.iter_errors(data), key=lambda err: (list(err.path), err.message))
        if errors:
            messages = [format_error(err) for err in errors]
            failures.append((example_path, messages))
            print(f"[FAIL] {example_path.name}")
            for message in messages:
                print(f"  - {message}")
        else:
            print(f"[PASS] {example_path.name}")

    if failures:
        print(f"\nValidation failed for {len(failures)} file(s).", file=sys.stderr)
        return 1

    print(f"\nValidated {len(example_files)} example file(s) successfully.")
    return 0


def format_error(error) -> str:
    path = "$" + "".join(f"/{segment}" for segment in error.absolute_path)
    return f"{path}: {error.message}"


if __name__ == "__main__":
    raise SystemExit(main())
