# SauceDemo Playwright Tests

[![Tests](https://github.com/rmarufs/saucedemo-playwright-tests/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/rmarufs/saucedemo-playwright-tests/actions/workflows/tests.yml)

E2E tests for [saucedemo.com](https://www.saucedemo.com) using Playwright and pytest (Python), with CI on GitHub Actions.

## Manual testing

Before automating, I tested the site manually. The documentation is in two Google Sheets:

- **[standard_user: checklist and 14 test cases](https://docs.google.com/spreadsheets/d/1UCCv4C8smS-dtVXMDwAdT8eiGUuKNRb_bhs6aGYIePE/edit?usp=sharing)**
- **[problem_user: checklist, 12 test cases (8 failed) and bug reports](https://docs.google.com/spreadsheets/d/1RyCtN0JOQxmbGCCnEZS-yXQnBAfl44qlwxKSQDxj6Lg/edit?usp=sharing)**

Defects were tracked in Jira (KAN-4 … KAN-8); the automated tests below reference these keys.

## Tech stack

- Python 3.12
- pytest
- Playwright (pytest-playwright)
- GitHub Actions

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
# Windows PowerShell
venv\Scripts\Activate.ps1
# Linux/macOS
source venv/bin/activate
```

Install dependencies and the browser:

```bash
pip install -r requirements.txt
playwright install chromium
```

## Running tests

```bash
pytest                  # headless
pytest --headed         # with a visible browser
pytest -rxX             # also show xfailed/xpassed reasons
pytest --browser firefox
```

## Test coverage

| Area | File | What is checked |
|------|------|-----------------|
| Login | `tests/test_login.py` | valid login, wrong password, locked-out user, empty fields, empty password |
| Cart | `tests/test_cart.py` | add one/two products, remove a product, product appears in the cart |
| Checkout | `tests/test_checkout.py` | full checkout, missing first name, missing postal code |
| Known bugs | `tests/test_problem_user.py` | see below |

### Known bugs of `problem_user`

Each test runs for two users via `pytest.mark.parametrize`:

- `standard_user`: the test passes, proving the check itself is correct;
- `problem_user`: marked `xfail(strict=True)`, because the bug is present.

With `strict=True`, a fixed bug turns the unexpected pass into a failure, so the suite signals when the `xfail` marker should be removed.

| Bug | Problem | Automated test |
|-----|---------|----------------|
| KAN-4 | Product images are duplicated | `test_product_images_are_unique` |
| KAN-5 | Sorting by name and price is incorrect | `test_products_sort_by_name_descending`, `test_products_sort_by_price_ascending` |
| KAN-6 | Not all products can be added to the cart | `test_all_products_can_be_added_to_cart` |
| KAN-7 | Bike Light opens incorrect product details | `test_bike_light_opens_its_product_details` |
| KAN-8 | Checkout swaps form field values | `test_checkout_keeps_customer_data_in_correct_fields` |

## CI

GitHub Actions runs the suite on every push and pull request to `main`. On failure, Playwright screenshots and traces are uploaded as artifacts.

## Project structure

```text
saucedemo-playwright-tests/
├── .github/workflows/tests.yml   # CI pipeline
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_problem_user.py
├── conftest.py                   # shared fixtures (logged_in_page, login_as)
├── pytest.ini
├── requirements.txt
└── README.md
```