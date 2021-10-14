from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(storage_state="auth-google-sangkyulee.json")

    # Open new page
    page = context.new_page()

    # Go to https://platform.grid.ai/
    page.goto("https://platform.grid.ai/")

    # Go to https://platform.grid.ai/#/
    page.goto("https://platform.grid.ai/#/")

    # Go to https://platform.grid.ai/#/dashboard
    page.goto("https://platform.grid.ai/#/dashboard")

    # Click [data-test-id="new-button"]
    page.click("[data-test-id=\"new-button\"]")

    # Click [data-test-id="start-menu-run"] >> text=Run
    page.click("[data-test-id=\"start-menu-run\"] >> text=Run")

    # Click text=At this rate, your credits will run out soon. Buy more credits to keep your jobs
    page.click("text=At this rate, your credits will run out soon. Buy more credits to keep your jobs")

    # Click [placeholder="Search..."]
    page.click("[placeholder=\"Search...\"]")

    # Click text=robert-s-lee/argecho
    page.click("text=robert-s-lee/argecho")

    # Click .repo-files-row-info
    page.click(".repo-files-row-info")

    # Click text=BetaUse Spot Instance >> :nth-match(span, 2)
    page.click("text=BetaUse Spot Instance >> :nth-match(span, 2)")

    # Click [data-test-id="submit-new-run"]
    page.click("[data-test-id=\"submit-new-run\"]")

    # Click text=/.*Successfully started run "precious-bettong-549".*/
    page.click("text=/.*Successfully started run \"precious-bettong-549\".*/")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)