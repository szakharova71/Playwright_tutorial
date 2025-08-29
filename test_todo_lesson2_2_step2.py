import re
from playwright.sync_api import Playwright, sync_playwright, expect

#use fixture from pytest-playwright
def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("1st playwright script")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()




