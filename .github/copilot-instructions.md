# Global Copilot Instructions

## AGENTS.md
The AGENTS.md file contains the main contextual instructions. It is located in the root directory.

# Project Guidelines

## Code Style
- Python code follows standard formatting with `black`/`flake8` conventions.
- Modules are small and focused; see `services/git_service.py` and `services/vector_store.py` for examples.
- Use type hints where reasonable; tests rely on straightforward function inputs/outputs.

## Architecture
- This is a lightweight Python package providing two core services accessible via an MCP server (`server.py`).
- Core logic lives under the `services/` package; tests mirror this layout under `tests/`.
- `config.json` contains environment-specific configuration (paths, API keys) read by `server.py`.
- The MCP server (`server.py`) wires up the services and is started by running `python server.py`.

## Build and Test
- Installation is via `pip install .` from the project root. Development extras include pytest (`pip install .[dev]`).
- Run unit tests with `pytest -q` from the workspace root; tests target `tests/test_git_service.py` and `tests/test_vector_store.py`.
- Agents should automatically attempt these commands when validating or changing code.

## Project Conventions
- The package is named `functional_expert`; top-level directory contains `pyproject.toml` and the source package.
- Service modules raise exceptions on errors; callers (including tests) assert on those conditions.
- Existing tests serve as the main examples of expected behavior and input/output shapes.

## Integration Points
- External dependencies are minimal and declared in `pyproject.toml`.
- `config.json` paths must be absolute; tests may construct temporary configurations.
- The MCP server exposes a single Python entry point defined in `server.py`.

## Security
- Sensitive values (OpenAI key) are stored in `config.json` and not checked into source control.
- Agents should not hardcode secrets; rely on environment or config.

> **Note:** No existing `.github/copilot-instructions.md` or agent files were present; this document provides all necessary guidance for AI coding agents in this workspace. Feel free to request clarifications or additions if any sections seem incomplete.