# Copilot Instructions for 2026-IS303-inclass

- This repository is a small set of introductory Python exercises, not a packaged application.
- Code lives in lesson folders: `Day 1/` and `Day 2/`. Each `*.py` is a standalone script that runs directly with `python3`.

## What to expect

- Files are simple, linear command-line programs using `input()` and `print()`.
- There is no build system, no tests, and no module/package structure.
- The repo is organized by day; use the folder name to infer lesson scope.

## Important patterns

- Numeric inputs are converted immediately with `int(input(...))`.
- Output is formatted with both string concatenation and f-strings.
- Variables are named to match prompt data, e.g. `name`, `grade1`, `credit1`, `age`.
- `Day 2/theme_park.py` is currently incomplete and should use `input(...)` calls, not bare references like `day_of_week = input`.

## How to run code

- Run individual scripts directly with:
  - `python3 "Day 1/gpa_calculator.py"`
  - `python3 "Day 2/theme_park.py"`
- Expect interactive prompts; verify behavior by entering sample values.

## Agent guidance

- Keep changes minimal and aligned to the script-style learning exercises.
- Do not introduce new project structure, package configuration, or frameworks.
- Preserve the existing input/output interaction model when fixing or extending scripts.
- If adding logic, keep it in the same file rather than splitting into modules.

## Notes for fixes

- When correcting scripts, focus on restoring prompt behavior and output formatting.
- There are no external integrations or dependencies beyond standard Python.
- Prefer readability and beginner-friendly code over compact tricks.
