# Overview
`chainliterate` is a teaching repository for how to build a robust AI-based chat platform using simple, well-chosen pieces of software and infrastructure using the Chainlit software package as its core.

Each chapter in this repository builds upon the previous one, gradually working up to a fully production-ready system with a number of features which makes it manageable to deploy such a system with a small team or single engineer.

# Getting started
This project targets macOS and Linux. It may work on Windows, but has not been tested. Use `uv` to manage Python, virtual environments, and dependencies. Ypu will also need Docker to complete all the chapters in this project; you can find the installation instructions [here](https://docs.docker.com/engine/install/).

You will also need to get an OpenRouter API key for all chapters and an AWS account to finish the later chapters.

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
