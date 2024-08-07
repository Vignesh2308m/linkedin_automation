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
    comp_list=["Deloitte","KPMG","EY","PwC"]
    for i in range(40):
        try:
            msg=comp_list[i%len(comp_list)]+" Data"
            page.goto("https://www.linkedin.com/mynetwork/grow/")
            page.get_by_placeholder("Search",exact=True).fill(msg)
            page.get_by_placeholder("Search",exact=True).press("Enter")
            time.sleep(2)
            page.get_by_role("link",name="See all people results").click()
            page.get_by_label("2nd").click()
            page.get_by_label("3rd+").click()
            time.sleep(2)
            page.get_by_role("button",name=re.compile("Connect",re.IGNORECASE)).first.click()
            page.get_by_label("Send without a note").click()
            time.sleep(10)
        except Exception as err:
            print(err)
            continue
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

