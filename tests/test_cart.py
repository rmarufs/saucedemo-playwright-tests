from playwright.sync_api import Page, expect


BACKPACK_NAME = "Sauce Labs Backpack"
BACKPACK_ADD_BUTTON = "[data-test='add-to-cart-sauce-labs-backpack']"


def test_adding_one_product_updates_cart_badge(logged_in_page: Page) -> None:
    logged_in_page.locator(BACKPACK_ADD_BUTTON).click()

    expect(logged_in_page.locator(".shopping_cart_badge")).to_have_text("1")


def test_adding_two_products_updates_cart_badge(logged_in_page: Page) -> None:
    logged_in_page.locator(BACKPACK_ADD_BUTTON).click()
    logged_in_page.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()

    expect(logged_in_page.locator(".shopping_cart_badge")).to_have_text("2")


def test_removing_product_from_catalog_hides_cart_badge(logged_in_page: Page) -> None:
    logged_in_page.locator(BACKPACK_ADD_BUTTON).click()
    logged_in_page.locator("[data-test='remove-sauce-labs-backpack']").click()

    expect(logged_in_page.locator(".shopping_cart_badge")).not_to_be_visible()


def test_added_product_is_shown_in_cart(logged_in_page: Page) -> None:
    logged_in_page.locator(BACKPACK_ADD_BUTTON).click()
    logged_in_page.locator(".shopping_cart_link").click()

    expect(
        logged_in_page.locator(".inventory_item_name").filter(has_text=BACKPACK_NAME)
    ).to_have_text(BACKPACK_NAME)
