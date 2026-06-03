# site
Plain Web Works marketing site and health check CLI.

## Plain Web Works Health Check

Install the local checker in a virtual environment:

```bash
python -m venv .venv
.venv/bin/python -m pip install -e .
```

Run the dogfood check for `plainwebworks.co`:

```bash
.venv/bin/plainwebworks-healthcheck
```

Client configuration lives in `clients.yml`. Daily JSON reports are written to `reports/daily/`, which is ignored by Git.
