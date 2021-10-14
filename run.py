from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(storage_state="auth.json")

    # Open new page
    page = context.new_page()

    # Go to https://platform.grid.ai/
    page.goto("https://platform.grid.ai/")

    # Go to https://platform.grid.ai/#/
    page.goto("https://platform.grid.ai/#/")

    # Go to https://platform.grid.ai/#/landing
    page.goto("https://platform.grid.ai/#/landing")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)