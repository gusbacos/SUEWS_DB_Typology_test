# SUEWS Database Test

This is a test repo for a database developed for SUEWS.

## Set up test environment

Recommended to use [`uv`](https://github.com/astral-sh/uv#getting-started) to create a virtual environment.

> [!NOTE]
> The instructions below are credited to [`uv`](https://github.com/astral-sh/uv#getting-started).


To create a virtual environment with `uv`:
```bash
uv venv
```

To activate the virtual environment:
```bash
# On macOS and Linux.
source .venv/bin/activate

# On Windows.
.venv\Scripts\activate
```

To generate a set of locked dependencies from an input file:
``` bash
uv pip compile requirements.in -o requirements.txt
```

To sync a set of locked dependencies with the virtual environment:
``` bash
uv pip sync requirements.txt
```