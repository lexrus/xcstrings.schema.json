# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Validation
- `python3 validate_examples.py` - Validates all example .xcstrings files against the schema
- `python3 validate_examples.py path/to/catalog.xcstrings` - Validates a specific catalog file
- `python3 -m json.tool <file>` - Pretty-prints JSON files for easier review

### Development Setup
- `python3 -m pip install jsonschema` - Installs the only required dependency

## Architecture

This repository implements a JSON Schema validator for Apple's .xcstrings string catalog format:

- **xcstrings.schema.json**: The core JSON Schema (Draft 7) defining the complete structure of .xcstrings files, including:
  - Root-level catalog properties (version, sourceLanguage, strings)
  - String entries with localizations, variations, and substitutions
  - Nested variation sets for pluralization and device-specific strings
  - State management for translation workflow (translated, needs_review, etc.)

- **validate_examples.py**: Validation script that:
  - Loads the schema using jsonschema's Draft7Validator
  - Iterates through all .xcstrings files in examples/
  - Reports validation status and detailed error messages
  - Returns non-zero exit code on validation failures

- **examples/**: Reference catalog files covering various real-world scenarios like:
  - Multi-language localizations
  - Plural variations
  - Format specifiers and substitutions
  - Different extraction states

## Key Implementation Details

The schema uses recursive definitions ($defs) to handle the nested nature of variations and substitutions. The validation enforces that localizations must have either a stringUnit or variations (but not neither).

When modifying the schema, always validate against all example files to ensure backward compatibility. New schema features should be accompanied by example files demonstrating their usage.