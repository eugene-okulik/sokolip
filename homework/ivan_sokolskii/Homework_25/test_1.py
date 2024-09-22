
from playwright.sync_api import Page, expect


def test_authentication(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    form_auth_button = page.get_by_role('link', name='Form Authentication')
    form_auth_button.click()
    user_name_field = page.get_by_role('textbox', name='username')
    user_name_field.fill('sokolip')
    password_field = page.get_by_role('textbox', name='password')
    password_field.fill('123456')
    login_button = page.get_by_role('button', name='Login')
    login_button.click()
