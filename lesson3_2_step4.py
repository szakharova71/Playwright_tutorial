def test_select(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#floatingSelect', value="3") #default by value
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")

def test_select_multiple(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#skills', value=["playwright", "python"])