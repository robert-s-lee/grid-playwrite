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

    # Go to https://platform.grid.ai/#/dashboard
    page.goto("https://platform.grid.ai/#/dashboard")

    # Click [data-test-id="new-button"]
    page.click("[data-test-id=\"new-button\"]")

    # Click [data-test-id="start-menu-run"] svg
    page.click("[data-test-id=\"start-menu-run\"] svg")

    # Click [data-test-id="run-name"]
    page.click("[data-test-id=\"run-name\"]")

    # Click [placeholder="Search..."]
    page.click("[placeholder=\"Search...\"]")

    # Click text=robert-s-lee/argecho
    page.click("text=robert-s-lee/argecho")

    # Click text=argecho.py
    page.click("text=argecho.py")

    # Click text=maincaret-down
    page.click("text=maincaret-down")

    # Click text=maincaret-down
    page.click("text=maincaret-down")

    # Click text=mainSelect a specific commit Id >> div
    page.click("text=mainSelect a specific commit Id >> div")

    # Click text=No Datastorecaret-down
    page.click("text=No Datastorecaret-down")

    # Click :nth-match(:text("sangkyulee@gmail.com: mnist"), 2)
    page.click(":nth-match(:text(\"sangkyulee@gmail.com: mnist\"), 2)")

    # Click text=3caret-down
    page.click("text=3caret-down")

    # Click :nth-match(:text("3"), 5)
    page.click(":nth-match(:text(\"3\"), 5)")

    # Click text=DatastoreName sangkyulee@gmail.com: mnistcaret-down.Version 3caret-down.Mount Di >> :nth-match(button, 3)
    page.click("text=DatastoreName sangkyulee@gmail.com: mnistcaret-down.Version 3caret-down.Mount Di >> :nth-match(button, 3)")

    # Click [placeholder="grid:sangkyulee@gmail.com: mnist:3"]
    page.click("[placeholder=\"grid:sangkyulee@gmail.com: mnist:3\"]")

    # Click text=BetaUse Spot Instance
    page.click("text=BetaUse Spot Instance")

    # Click text=BetaUse Spot Instance
    page.click("text=BetaUse Spot Instance")

    # Click text=BetaUse Spot Instance >> :nth-match(span, 2)
    page.click("text=BetaUse Spot Instance >> :nth-match(span, 2)")

    # Click text=Grid Cloudcaret-down
    page.click("text=Grid Cloudcaret-down")

    # Click text=Grid Cloudcaret-down
    page.click("text=Grid Cloudcaret-down")

    # Click text=Grid Cloudcaret-down
    page.click("text=Grid Cloudcaret-down")

    # Click :nth-match(:text("Grid Cloud"), 2)
    page.click(":nth-match(:text(\"Grid Cloud\"), 2)")

    # Click text=2xCPU (2 GB) $0.02/h (t2.medium)caret-down
    page.click("text=2xCPU (2 GB) $0.02/h (t2.medium)caret-down")

    # Click text=4xCPU (4 GB) $0.06/h (t2.xlarge)
    page.click("text=4xCPU (4 GB) $0.06/h (t2.xlarge)")

    # Click text=1caret-down
    page.click("text=1caret-down")

    # Click a:has-text("2")
    page.click("a:has-text(\"2\")")

    # Click input[name="diskSize"]
    page.click("input[name=\"diskSize\"]")

    # Click input[name="diskSize"]
    page.click("input[name=\"diskSize\"]")

    # Fill input[name="diskSize"]
    page.fill("input[name=\"diskSize\"]", "150")

    # Click text=Grid Searchcaret-down
    page.click("text=Grid Searchcaret-down")

    # Click text=Random Search
    page.click("text=Random Search")

    # Click text=lightningcaret-down
    page.click("text=lightningcaret-down")

    # Click text=torch
    page.click("text=torch")

    # Click textarea
    page.click("textarea")

    # Click text=BOOLEAN--use_batchnorm >> button
    page.click("text=BOOLEAN--use_batchnorm >> button")

    # Click textarea
    page.click("textarea")

    # Click textarea
    page.click("textarea", button="right")

    # Fill textarea
    page.fill("textarea", "--use_batchnorm ")

    # Click text=INTEGER--batch_size64 >> button
    page.click("text=INTEGER--batch_size64 >> button", button="right")

    # Click text=INTEGER--batch_size64 >> button
    page.click("text=INTEGER--batch_size64 >> button")

    # Click textarea:has-text("--use_batchnorm")
    page.click("textarea:has-text(\"--use_batchnorm\")")

    # Click textarea:has-text("--use_batchnorm")
    page.click("textarea:has-text(\"--use_batchnorm\")", button="right")

    # Fill textarea:has-text("--use_batchnorm")
    page.fill("textarea:has-text(\"--use_batchnorm\")", "--use_batchnorm --batch_size 64")

    # Click text=FLOAT--learning_rate 0.1 | 1e-2 >> button
    page.click("text=FLOAT--learning_rate 0.1 | 1e-2 >> button")

    # Click text=--use_batchnorm --batch_size 64
    page.click("text=--use_batchnorm --batch_size 64")

    # Fill text=--use_batchnorm --batch_size 64
    page.fill("text=--use_batchnorm --batch_size 64", "--use_batchnorm --batch_size 64 ")

    # Click text=--use_batchnorm --batch_size 64
    page.click("text=--use_batchnorm --batch_size 64", button="right")

    # Fill text=--use_batchnorm --batch_size 64
    page.fill("text=--use_batchnorm --batch_size 64", "--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2")

    # Click text=STRING--model_name bert >> button
    page.click("text=STRING--model_name bert >> button")

    # Click text=STRING--model_name bert >> button
    page.click("text=STRING--model_name bert >> button", button="right")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2")

    # Fill text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2
    page.fill("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2", "--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 ")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2", button="right")

    # Fill text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2
    page.fill("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2", "--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert")

    # Click .flag-holder .flag-terminal .sc-kGXeez
    page.click(".flag-holder .flag-terminal .sc-kGXeez")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert")

    # Fill text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert
    page.fill("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert", "--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert ")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert", button="right")

    # Fill text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert
    page.fill("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert", "--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --argument \"[32, 64, 128]\"")

    # Click div:nth-child(7) .flag-holder .flag-terminal .sc-kGXeez
    page.click("div:nth-child(7) .flag-holder .flag-terminal .sc-kGXeez")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a")

    # Press ArrowRight
    page.press("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a", "ArrowRight")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a")

    # Click text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a
    page.click("text=--use_batchnorm --batch_size 64 --learning_rate 0.1 | 1e-2 --model_name bert --a")

    # Click input[name="trials"]
    page.click("input[name=\"trials\"]")

    # Fill input[name="trials"]
    page.fill("input[name=\"trials\"]", "05")

    # Click text=torchcaret-down
    page.click("text=torchcaret-down")

    # Click text=torchcaret-down
    page.click("text=torchcaret-down")

    # Click [data-test-id="submit-new-run"]
    page.click("[data-test-id=\"submit-new-run\"]")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)