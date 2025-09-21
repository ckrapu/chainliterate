![Getting Started Diagram](diagram-01.svg)

# `01-getting-started`
This chapter requires a working installation of `uv` and a virtual environment (ideally located at `.venv/`) in this folder. It does not use Docker.

# Instructions
Review the code in `app.py` as well as the system diagram shown above. It is strongly recommended that you type the code verbatim into a new file to help with understanding and retention. Boot the application with the following command and make sure it is functional.
```
uv run chainlit run app.py -w
```

Then, work on the exercises below.

# Exercises
1. **Generation statistics**: You can configure Chainlit to render HTML directly in a Message. Edit the settings in `.chainlit/config.toml` to enable showing HTML and write a helper function `add_stats` that counts the emitted tokens and records the length of time required from start-to-finish for answer generation. This function should style a short message that is appended to the end of every LLM response that shows how long it took to generate and the number of tokens generated.

2. **Logging levels**: Use the `logging` library at `INFO` level for the following:
  - Show one logging message for application startup (after imports, outside of the @-decorated functions) to report on the model used by the app as well as the base URL
  - Show a logging message that reports on the user session ID via `{cl.user_session.get('id')}` in `on_chat_start`
  - Add a logging message for `on_message` which reports the number of tokens and time elapsed.

3. **Credential check**: Add a check for `config.api_key` to make sure it is not None or `''` at startup, and exit the application with an error message if it is. Note that you can test this condition using just `if config.api_key:`.

4. **Multi-turn**: The starter app does not fully support multi‑turn conversation because assistant turns are not stored in the message history. Update the code so that `history` alternates between `user` and `assistant` messages. The `history` variable should look like the following with alternating messages:
```
[ 
  {"role": "user", "content": '...'},
  {"role": "assistant", "content": '...'},
  {"role": "user", "content": '...'}
]
```
Edit the `cl.user_session` to store a value labeled `"history"` which contains these alternating messages.

5. **Reset command**: Add a `/reset` slash command that clears the current conversation history while preserving the active system prompt and runtime settings. When invoked, rebuild `cl.user_session["history"]` to include only the existing system message, send a short confirmation message to the user, and log the reset at `INFO` with the session ID.
