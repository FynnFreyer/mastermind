# Mastermind

A simple showcase implementation of the classic Mastermind game.

## Overview

This repository contains a small, self-contained Python package and CLI that plays a round of Mastermind in the terminal.
It showcases basic package structure, simple game logic, a CLI entry point, and common Python project tooling (formatting, linting, type checking, and tests scaffolding).

### Links

- [Repository](https://github.com/FynnFreyer/mastermind)
- [Issues](https://github.com/FynnFreyer/mastermind/issues)

### Game

Current game flow:

- A CodeMaker generates a hidden code of colored pegs.
- A CodeBreaker generates guesses (currently random).
- The Board keeps track of turns and prints a simple textual board after each turn.
- The game ends when the guess matches the code or the board fills up.

Status: Alpha (API and behavior may change).

### Tech stack

- Language: Python (>= 3.9)
- Packaging/build: pyproject.toml with Hatchling
- CLI entry point: console script `mastermind` (or `python -m mastermind`)
- Tooling for development
    - `make` (automate the rest),
    - `ruff` (lint),
    - `isort` (import),
    - `autopep8` (format),
    - `mypy` (type check),
    - `pytest` (test),
    - `uv` (manage dependencies)
- No runtime dependencies so far (the game only uses the standard library)

## Installation

You can install the project with pip.

```bash
# (Optional, but recommended)
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # on macOS/Linux
# Install the mastermind package
pip install .
```

## Running

After installing, you can run the CLI in two ways:

- Via the console script `mastermind`
- Via the `mastermind.__main__` module with `python -m mastermind`

See `mastermind --help` for usage and options.
Exit status: 0 on win; non-zero on loss or error.

## Development

First, create and activate a virtual environment.

```bash
make install      # install dependencies (including dev stuff)
pip install -e .  # editable project install for fast iteration
```

> ![Notes]
>
> Common tasks are automated via the Makefile.
> Ensure your venv is active and run `make help` to see all available targets.
>
> - Regenerate lock files and update the environment with `make update`
> - Before opening a PR run `make chores` and fix any issues

### Tests

- Pytest is configured via the Makefile (`make test`).
- Currently, there are no test modules in the repository.  
  **TODO**: Add tests covering Board, Peg, Player strategies, and CLI.

### Project structure

#### Modules

Abridged layout:

- `mastermind/`
    - `__init__.py`
    - `__about__.py`
    - `__main__.py` - CLI entry point (provides console script)
    - `app.py` - contains basic game logic
    - `board.py` - board state (and basic CLI rendering)
    - `peg.py` - `CodePeg` and `KeyPeg` enums and type aliases
    - `player.py` - `CodeMaker`/`CodeBreaker` logic
- `Makefile` - chores and dependency management
- `pyproject.toml` - project metadata, build backend, tools config
- `requirements.txt` - runtime requirements (currently empty)
- `requirements-dev.txt` - development dependencies
- `LICENSE`
- `README.md`

### Packaging and release

- **TODO**: CI workflow for publishing to PyPI
- **TODO**: Sphinx setup for generating docs
- **TODO**: CI workflow for publishing documentation

## License

MIT License.
See the LICENSE file for details.
