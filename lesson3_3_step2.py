from playwright.sync_api import Page, expect

def test_navigates_to_login_page(page):
    response = page.request.get('https://playwright.dev')
    expect(response, "error found").to_be_ok()


def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.locator("h2").is_visible()

def test_add_todo_assert(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    assert page.locator("h2").is_visible(), "assert fail"

def test_add_todo_expect(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page.locator('h2'),"expect fail").to_be_visible()