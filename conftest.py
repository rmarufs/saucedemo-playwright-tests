from collections.abc import Callable

import pytest
from playwright.sync_api import Page


@pytest.fixture
def logged_in_page(page: Page) -> Page:
    """Return a page logged in as the standard SauceDemo user."""
    page.goto("/")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    return page


@pytest.fixture
def login_as(page: Page) -> Callable[[str], Page]:
    def login(username: str) -> Page:
        page.goto("/")
        page.locator("[data-test='username']").fill(username)
        page.locator("[data-test='password']").fill("secret_sauce")
        page.locator("[data-test='login-button']").click()
        return page

    return login
