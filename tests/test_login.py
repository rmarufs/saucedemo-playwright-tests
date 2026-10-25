from playwright.sync_api import Page, expect


def login(page: Page, username: str, password: str) -> None:
    page.locator("[data-test='username']").fill(username)
    page.locator("[data-test='password']").fill(password)
    page.locator("[data-test='login-button']").click()


def test_standard_user_can_log_in(page: Page) -> None:
    page.goto("/")

    login(page, "standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_login_shows_error_for_invalid_password(page: Page) -> None:
    page.goto("/")

    login(page, "standard_user", "invalid_password")

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Username and password do not match"
    )


def test_locked_out_user_cannot_log_in(page: Page) -> None:
    page.goto("/")

    login(page, "locked_out_user", "secret_sauce")

    expect(page.locator("[data-test='error']")).to_contain_text(
        "this user has been locked out"
    )


def test_login_shows_error_when_fields_are_empty(page: Page) -> None:
    page.goto("/")

    login(page, "", "")

    expect(page.locator("[data-test='error']")).to_contain_text("Username is required")


def test_login_shows_error_when_password_is_empty(page: Page) -> None:
    page.goto("/")

    login(page, "standard_user", "")

    expect(page.locator("[data-test='error']")).to_contain_text("Password is required")
