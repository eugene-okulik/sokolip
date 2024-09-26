from playwright.sync_api import Page, Dialog, expect, BrowserContext


def test_click_alert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')

    def accept_alert(alert: Dialog):
        alert.accept()

    page.on("dialog", accept_alert)
    click_button = page.get_by_role('link', name='Click')
    click_button.click()
    after_click_text = page.locator("//p[@id='result-text']")
    expect(after_click_text).to_have_text('Ok')


def test_check_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        link.click()

    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    check_button = page.get_by_role('link', name='Click')
    expect(check_button).to_be_enabled()


def test_change_button_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button_locator = page.get_by_role('button', name='Color Change')
    expect(button_locator).to_have_css('color', 'rgb(220, 53, 69)')
    button_locator.click()
