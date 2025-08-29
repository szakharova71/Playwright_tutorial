def test_dialogs(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()

def test_dialogs1(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept()) #accept 2nd alert
    page.on("dialog", lambda dialog: print(dialog.message)) #print dialog text
    page.get_by_text("Диалог Confirmation").click()

def test_dialogs2(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.dismiss()) #dismiss 2nd alert
    page.get_by_text("Диалог Confirmation").click()

def test_dialogs3(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept("test value")) #enter "test value" into prompt
    page.get_by_text("Диалог Prompt").click()