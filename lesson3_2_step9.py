def test_get_all_text(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_inner_texts())

def test_get_all_text1(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_text_contents())