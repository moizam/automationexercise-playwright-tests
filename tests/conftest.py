import pytest
import allure
from playwright.sync_api import sync_playwright
import os

IS_CI = os.getenv("GITHUB_ACTIONS") == "true"

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # Launching with maximized settings
        browser = p.chromium.launch(headless=IS_CI, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.set_default_timeout(60000)
        page.set_default_navigation_timeout(60000)

        yield page

        page.close()
        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshot on failure for Allure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Access the 'page' fixture from the test item
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )