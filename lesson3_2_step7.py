def test_upload(page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files("#formFile", "test.txt")
    page.locator("#file-submit").click()

def test_upload1(page):
    page.goto('https://zimaev.github.io/upload/')
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("test.txt"))
    page.locator("#formFile").click()

def test_upload2(page):
    page.goto('https://zimaev.github.io/upload/')
    with page.expect_file_chooser() as fc_info:
        page.locator("#formFile").click()
    file_chooser = fc_info.value
    file_chooser.set_files("test.txt")