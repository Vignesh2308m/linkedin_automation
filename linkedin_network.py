import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.linkedin.com/")
    page.get_by_role("link", name="Sign in", exact=True).click()
    page.get_by_label("Email or phone").click()
    page.get_by_label("Email or phone").fill("vicky.manoharan2018@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Nila@09122000")
    page.get_by_label("Sign in", exact=True).click()
    time.sleep(20)
    page.goto("https://www.linkedin.com/mynetwork/grow/")
    print(page.get_by_role("main").locator("div").all())
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

