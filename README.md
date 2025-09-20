# XCStrings Schema

A JSON Schema and validation helper for Apple's `.xcstrings` string catalog files. The schema mirrors the structure observed in real-world catalogs and can be used with [`jsonschema`](https://python-jsonschema.readthedocs.io/) or any compatible validator to ensure catalogs remain well-formed.

> IMPORTANT: The included schema may be out of date; verify against your catalogs before relying on it.

## Project Layout

- `examples/` — sample `.xcstrings` catalogs gathered from various scenarios.
- `xcstrings.schema.json` — JSON Schema describing the catalog format.
- `validate_examples.py` — helper script that validates every example file against the schema.

## Getting Started

1. Install the Python dependency (only `jsonschema` is required):

   ```bash
   python3 -m pip install jsonschema
   ```

2. Validate the bundled example catalogs:

   ```bash
   python3 validate_examples.py
   ```

   All example catalogs should report `PASS`. The script exits with a non-zero status if any validation fails.

3. Validate your own catalog by copying it into the `examples/` directory (or by adapting the script for your workflow) and re-running the command above.

## Using the Schema Elsewhere

The schema can be consumed by any tooling that understands JSON Schema Draft 7. For instance, in Python:

```python
from jsonschema import Draft7Validator
import json

with open("xcstrings.schema.json") as schema_file:
    schema = json.load(schema_file)

with open("MyCatalog.xcstrings") as catalog_file:
    data = json.load(catalog_file)

Draft7Validator(schema).validate(data)
```

## Contributing

Feel free to open issues or pull requests with additional test catalogs, expanded schema coverage, or documentation fixes.

## License

Released under the MIT License. See [LICENSE](LICENSE).
