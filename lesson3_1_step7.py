
#pseudo classes
def test_locators(page):
    page.goto("https://zimaev.github.io/table-1/")
    right_tab=page.locator("td:right-of(td p:text('Software engineer'))")
    left_tab=page.locator("td:left-of(td p:text('Software engineer'))")
    above_consultant=page.locator("td:above(td p:text('Consultant'))")
    below_consultant=page.locator("td:below(td p:text('Consultant'))")
    near_consultant=page.locator("td:near(td p:text('Consultant'))")

    #log_or_sign_in=page.locator('button:has-text("Log in"), button:has-text("Sign in")').click()





