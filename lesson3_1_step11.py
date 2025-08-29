def test_checkboxes(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    checkbox = page.locator("input")
    for i in range(checkbox.count()):
        checkbox.nth(i).click()

def test_checkboxes1(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.get_by_name
    checkboxes = page.locator("input")
    for checkbox in checkboxes.all():
        checkbox.check()

def test_checkboxes2(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()

def test_checkboxes3(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").click()
    page.locator("text=Checked checkbox").click()
    page.locator("text=Default radio").click()
    page.locator("text=Default checked radio").click()
    page.locator("text=Checked switch checkbox input").click()