# SauceDemo Playwright Tests

E2E tests for saucedemo.com using Playwright and pytest.

## Tech stack

- Python
- pytest
- Playwright
- pytest-playwright

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
# Windows PowerShell
venv\Scripts\Activate.ps1
# Linux/macOS
source venv/bin/activate
```

Install dependencies and browser binaries:

```bash
pip install -r requirements.txt
playwright install
```

## Running tests

```bash
pytest
pytest --headed
pytest --browser firefox
```

## Project structure

```text
saucedemo-playwright-tests/
├── tests/
│   └── __init__.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Test coverage

- Successful login with `standard_user`.
- Error for an invalid password.
- Error for the locked `locked_out_user` account.
- Error when both login fields are empty.
- Error when the password is empty.
