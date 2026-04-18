---
name: use-uv
description: Always use uv for Python work. Use when Python code, dependencies, virtual environments, scripts, or Python CLI tools are involved.
---

Do not call `python`, `pip`, `venv`, `virtualenv`, `poetry`, or `pipx` directly unless the user explicitly asks. Use `uv` instead.
Start new Python projects with `uv init`.
Add dependencies with `uv add` and remove them with `uv remove`.
Run Python scripts and project tools with `uv run`, including `pytest`, `mypy`, and `python -m` equivalents.
Use `uv sync` to install and align the environment with the lockfile.
Use `uv run --with <package>` for one-off dependencies when you do not need to modify the project.
Use `uvx <tool>` for one-off Python CLI tools that are not part of the project.
Use `uv pip` only for legacy pip-compatible workflows when `uv add` or `uv sync` cannot be used.
