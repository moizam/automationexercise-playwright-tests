import time
import pytest
from playwright.sync_api import expect

def get_data():
    return [
        ("Fancy Green Top 123456"),
        ("Fancy Green Top"),
        ("Blue")
    ]

@pytest.mark.parametrize("product_search", get_data())
def test_add_to_cart(page,product_search):

    # Open the website
    page.goto("https://automationexercise.com/")

    # Navigate to the Products page
    page.click("[href='/products']")
    expect(page).to_have_url("https://automationexercise.com/products")  # Check, navigated to correct page

    # Search for a product

    page.fill("#search_product",product_search)
    page.click("#submit_search")

    # Wait for products to load
    products = page.locator("//div[@class='single-products']")
    products.first.wait_for(timeout=5000)


    # Find the correct product from list and click Add to Cart
    product_found = False
    for i in range(products.count()):
        p_text = products.nth(i).locator(".productinfo p").inner_text()
        if p_text == product_search:
            products.nth(i).locator(".productinfo a").click()
            product_found = True
            break
    # Assert that the product was found
    assert product_found, f"Product '{product_search}' not found on Products page"

    # Click 'View Cart' in the modal
    page.click("//div[@id='cartModal']//a[@href='/view_cart']")

    # Wait for cart items table to load
    items = page.locator("//table[@id='cart_info_table']//td[@class='cart_description']//h4//a")
    items.first.wait_for(timeout=30000)
    # find product names in the cart
    product_found = False
    for i in range(items.count()):
        text = items.nth(i).inner_text()  # fetch the visible text
        if text == product_search:
            product_found = True

    # Assert product is in cart
    assert product_found, f"Product '{product_search}' not found in cart!"



