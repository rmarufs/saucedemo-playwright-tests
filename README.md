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
- Adding one or two products to the cart.
- Removing a product from the catalog.
- Displaying an added product in the cart.
- Completing checkout with valid customer information.
- Checkout validation for missing first name and postal code.

### problem_user known bugs

The following checks run for `standard_user` and are strict `xfail` cases for
`problem_user` until the corresponding defect is fixed:

- [KAN-4](#kan-4): unique product images.
- [KAN-5](#kan-5): sorting by name and price.
- [KAN-6](#kan-6): adding all products to the cart.
- [KAN-7](#kan-7): opening the Sauce Labs Bike Light details.
- [KAN-8](#kan-8): preserving checkout form values.

#### KAN-4

All six catalog product images have unique sources.

#### KAN-5

Products sort correctly by name and price.

#### KAN-6

All six catalog products can be added to the cart.

#### KAN-7

The Sauce Labs Bike Light link opens its own details and price.

#### KAN-8

Checkout preserves first-name and last-name field values before continuing.
