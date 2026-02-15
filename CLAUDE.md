# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What is this project

An MCP (Model Context Protocol) server that exposes Internet Archive search and retrieval capabilities as tools for LLM agents. The server lets any MCP-compatible client (Claude Desktop, Claude Code, etc.) search the Internet Archive for images, with audio and video support planned.

## Commands

```bash
uv sync                                  # Install dependencies
uv run pytest                            # Run all tests
uv run pytest tests/test_search.py       # Run a single test file
uv run pytest -k "test_name"             # Run a single test by name
uv run ruff check .                      # Lint
uv run ruff format .                     # Format
```

## Architecture

Source lives in `src/ia_mcp/` (hatchling `src` layout, Python >=3.11). The server uses the `mcp` Python SDK and communicates over stdio.

### Key components

- `server.py` — MCP server entry point. Registers tools and handles requests.
- `tools/` — One module per tool category (e.g. `search_images.py`). Each module defines tool schemas and handler functions.
- `ia_client.py` — Thin wrapper around the `internetarchive` Python library. Handles search queries, item retrieval, and metadata extraction.
- `config.py` — Server configuration (defaults, supported collections, license filters).

## Development Workflow

Follow TDD: write tests first, then implement, then run `uv run pytest`, then `uv run ruff check . && uv run ruff format .`.

## Code Conventions

- Type hints on all function signatures
- Docstrings on public functions and classes
- Prefer list comprehensions over for-loop-append patterns when the result is clean and readable
- Ruff enforces PEP 8 with 79-char line length (rules: E, F, I, W)
- Tests in `tests/` mirroring `src/` structure

## Test Conventions

- Mock the `internetarchive` library calls in unit tests — don't hit the real API by default
- Integration tests that hit the real IA API should be marked with `@pytest.mark.integration` so they can be skipped in CI
- Use `tmp_path` for any filesystem assertions

## Writing Style

- README and docs should be practical, not didactic. Describe what things do, skip design rationale.
- Avoid "code lecture" tone.
