from playwright.sync_api import Page, Dialog, expect


def test_click_alert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')

    def accept_alert(alert: Dialog):
        alert.accept()

    page.on("dialog", accept_alert)
    click_button = page.get_by_role('link', name='Click')
    click_button.click()
    after_click_text = page.locator("//p[@id='result-text']")
    expect(after_click_text).to_have_text('Ok')

def test_check_tab(page: Page):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')

