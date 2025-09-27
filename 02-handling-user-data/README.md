# Overview
This chapter focuses on handling user data across sessions while keeping the app simple to run locally. You will run a Chainlit app backed by Postgres (via Docker), and use OpenRouter for model access. To enable persistence across sessions, Chainlit requires a PostgreSQL database, a blob storage resource, and credentials for an OAuth2 client. We'll work on enabling data persistence in this chapter.

# Prerequisites
- Docker and Docker Compose installed
- `uv` installed for Python env + dependency management
- An OpenRouter API key
- A Google Cloud Platform OAuth client set up [(instructions here)](https://support.google.com/cloud/answer/15549257?hl=en); you should have values available for `OAUTH_GOOGLE_CLIENT_ID` and 
`OAUTH_GOOGLE_CLIENT_SECRET`.

# Environment Setup
- From the project root, copy the example env file and set secrets:
  - `cp .env.example .env`
  - Open `.env` and set `OPENROUTER_API_KEY` (required)
  - Set/confirm:
    - `CHAINLIT_AUTH_SECRET` (you can generate one with `chainlit create-secret`)
    - `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` (default DB is `chainliterate_db`)
    - `DATABASE_URL` should match your Postgres settings
- Create a virtual environment with the following commands:
  - `uv venv`
  - `source .venv/bin/activate`
  - `uv sync`
- Start Postgres and LocalStack for mimicking AWS S3 with `docker compose up`

After finishing these steps, you can run the app in hot reload mode with `uv run chainlit run app.py -w` and you should be greeted with a login page.

# Exercises