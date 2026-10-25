from playwright.sync_api import Page, expect


BACKPACK_ADD_BUTTON = "[data-test='add-to-cart-sauce-labs-backpack']"


def start_checkout(page: Page) -> None:
    page.locator(BACKPACK_ADD_BUTTON).click()
    page.locator(".shopping_cart_link").click()
    page.locator("[data-test='checkout']").click()


def test_user_can_complete_checkout(logged_in_page: Page) -> None:
    start_checkout(logged_in_page)
    logged_in_page.locator("[data-test='firstName']").fill("Jane")
    logged_in_page.locator("[data-test='lastName']").fill("Doe")
    logged_in_page.locator("[data-test='postalCode']").fill("12345")
    logged_in_page.locator("[data-test='continue']").click()
    logged_in_page.locator("[data-test='finish']").click()

    expect(logged_in_page.locator(".complete-header")).to_have_text(
        "Thank you for your order!"
    )


def test_checkout_shows_error_when_form_is_empty(logged_in_page: Page) -> None:
    start_checkout(logged_in_page)
    logged_in_page.locator("[data-test='continue']").click()

    expect(logged_in_page.locator("[data-test='error']")).to_contain_text(
        "First Name is required"
    )


def test_checkout_shows_error_when_postal_code_is_empty(logged_in_page: Page) -> None:
    start_checkout(logged_in_page)
    logged_in_page.locator("[data-test='firstName']").fill("Jane")
    logged_in_page.locator("[data-test='lastName']").fill("Doe")
    logged_in_page.locator("[data-test='continue']").click()

    expect(logged_in_page.locator("[data-test='error']")).to_contain_text(
        "Postal Code is required"
    )
