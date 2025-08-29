
def test_chain(page):
    page.goto("https://zimaev.github.io/navbar/")
    page.locator("#navbarNavDropdown >> li:has-text('Company')").click()

def test_filter(page):
    page.goto("https://zimaev.github.io/filter/")
    #page.locator("li").filter(has_text='Company').click()

    #page.locator('li').filter(has=page.locator('.dropdown-toggle')).click()

    row_locator = page.locator("tr")
    row_locator.filter(has_not=page.get_by_role("button")).count()

    row_locator.filter(has_not_text="helicopter")

    #row_locator \
    #.filter(has_text="text in column 1") \
    #.filter(has=page.get_by_role("button", name="column 2 button")) \
    #.click()



