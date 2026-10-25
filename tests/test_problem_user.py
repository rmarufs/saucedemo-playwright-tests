from collections.abc import Callable

import pytest
from playwright.sync_api import Page, expect


USERS = [
    "standard_user",
    pytest.param(
        "problem_user",
        marks=pytest.mark.xfail(
            strict=True,
            reason="KAN-4: problem_user displays duplicate product images",
        ),
    ),
]


def begin_checkout(page: Page) -> None:
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator(".shopping_cart_link").click()
    page.locator("[data-test='checkout']").click()


@pytest.mark.parametrize("username", USERS)
def test_product_images_are_unique(
    login_as: Callable[[str], Page], username: str
) -> None:
    page = login_as(username)
    product_images = page.locator("img.inventory_item_img")
    expect(product_images).to_have_count(6)
    image_sources = product_images.evaluate_all(
        "images => images.map(image => image.src)"
    )

    assert len(image_sources) == len(set(image_sources))


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param(
            "problem_user",
            marks=pytest.mark.xfail(
                strict=True,
                reason="KAN-5: problem_user does not sort products by name correctly",
            ),
        ),
    ],
)
def test_products_sort_by_name_descending(
    login_as: Callable[[str], Page], username: str
) -> None:
    page = login_as(username)
    page.locator("[data-test='product-sort-container']").select_option("za")
    product_names = page.locator("[data-test='inventory-item-name']")

    expect(product_names.first).to_have_text("Test.allTheThings() T-Shirt (Red)")
    expect(product_names.last).to_have_text("Sauce Labs Backpack")


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param(
            "problem_user",
            marks=pytest.mark.xfail(
                strict=True,
                reason="KAN-5: problem_user does not sort products by price correctly",
            ),
        ),
    ],
)
def test_products_sort_by_price_ascending(
    login_as: Callable[[str], Page], username: str
) -> None:
    page = login_as(username)
    page.locator("[data-test='product-sort-container']").select_option("lohi")
    product_prices = page.locator("[data-test='inventory-item-price']")

    expect(product_prices.first).to_have_text("$7.99")
    expect(product_prices.last).to_have_text("$49.99")


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param(
            "problem_user",
            marks=pytest.mark.xfail(
                strict=True,
                reason="KAN-6: problem_user cannot add every product to the cart",
            ),
        ),
    ],
)
def test_all_products_can_be_added_to_cart(
    login_as: Callable[[str], Page], username: str
) -> None:
    page = login_as(username)
    product_slugs = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket",
        "sauce-labs-onesie",
        "test.allthethings()-t-shirt-(red)",
    ]

    for slug in product_slugs:
        page.locator(f"[data-test='add-to-cart-{slug}']").click()
        expect(page.locator(f"[data-test='remove-{slug}']")).to_be_visible()

    expect(page.locator(".shopping_cart_badge")).to_have_text("6")


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param(
            "problem_user",
            marks=pytest.mark.xfail(
                strict=True,
                reason="KAN-7: problem_user opens incorrect Bike Light product details",
            ),
        ),
    ],
)
def test_bike_light_opens_its_product_details(
    login_as: Callable[[str], Page], username: str
) -> None:
    page = login_as(username)
    page.locator("[data-test='item-0-title-link']").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=0")
    expect(page.locator("[data-test='inventory-item-name']")).to_have_count(1)

    expect(page.locator("[data-test='inventory-item-name']")).to_have_text(
        "Sauce Labs Bike Light"
    )
    expect(page.locator("[data-test='inventory-item-price']")).to_have_text("$9.99")


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        pytest.param(
            "problem_user",
            marks=pytest.mark.xfail(
                strict=True,
                reason="KAN-8: problem_user swaps checkout form field values",
            ),
        ),
    ],
)
def test_checkout_keeps_customer_data_in_correct_fields(
    login_as: Callable[[str], Page], username: str
) -> None:
    page = login_as(username)
    begin_checkout(page)
    first_name = page.locator("[data-test='firstName']")
    last_name = page.locator("[data-test='lastName']")
    first_name.fill("Test")
    last_name.fill("User")
    page.locator("[data-test='postalCode']").fill("12345")

    expect(first_name).to_have_value("Test")
    expect(last_name).to_have_value("User")
    page.locator("[data-test='continue']").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
