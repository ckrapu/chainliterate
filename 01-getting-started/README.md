# Overview
`chainliterate` is a proof-of-concept for a platform built on open souce code and components to provide artificial intelligence as a public good and respecting data privacy requirements.

The core architecture of this repository involves several pieces:
- Currently, large language model (LLM) inference is handled using OpenRouter to connect to a range of vendors.
- The user interface and application logic is provided by [Chainlit](https://docs.chainlit.io/get-started/overview)
- Data persistence and storage is managed by AWS Aurora and Amazon S3
- The site is hosted on AWS Amplify

# Getting started
This project targets macOS and Linux. Use `uv` to manage Python, virtual environments, and dependencies.

## Installing uv
- macOS (Homebrew): `brew install uv`
- macOS/Linux (official script): `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Verify: `uv --version`

If the script install doesn’t put `uv` on your PATH, add `~/.local/bin` to your PATH (e.g., `export PATH="$HOME/.local/bin:$PATH"`).

## Creating a virtual environment
- From the project root: `uv venv`
- Activate (optional; `uv` can run commands without activation):
  - macOS/Linux (bash/zsh): `source .venv/bin/activate`

## Installing dependencies
`uv sync`
  - Adds missing dependencies and locks them; re-run after changes.

Tip: To add a new runtime dependency: `uv add <package>`; for dev-only: `uv add --dev <package>`.
