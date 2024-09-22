from playwright.sync_api import Page
import time

name = "Ivan"
last_name = "Ivanov"
user_email = "123@ya.ru"
mobile_phone = "1234567891"
current_address = "Cancun"


def test_student_registration_page(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    name_field = page.get_by_placeholder('First name')
    name_field.fill(name)
    last_name_field = page.get_by_placeholder('Last Name')
    last_name_field.fill(last_name)
    email_field = page.get_by_placeholder('name@example.com')
    email_field.fill(user_email)
    gender_checkbox = page.locator("//label[@for='gender-radio-1']")
    gender_checkbox.click()
    mobile_number_field = page.get_by_placeholder('Mobile Number')
    mobile_number_field.fill(mobile_phone)
    dob_fieild = page.locator("//input[@id='dateOfBirthInput']")
    dob_fieild.click()
    page.select_option("//select[@class ='react-datepicker__year-select']", '2004')
    page.select_option("//select[@class='react-datepicker__month-select']", 'May')
    page.locator("//div[@class='react-datepicker__day react-datepicker__day--004']").click()
    subjects = page.locator("//input[@id='subjectsInput']")
    subjects.click()
    subjects.fill('en')
    page.locator("//div[text()='English']").click()
    hobbies = page.locator("//label[@for='hobbies-checkbox-1']")
    hobbies.click()
    current_add_field = page.get_by_placeholder('Current Address')
    current_add_field.fill(current_address)
    state_selector = page.locator("//div[@id='state']")
    time.sleep(2)
    state_selector.click()
    time.sleep(3)
    page.locator("//div[text()= 'NCR']").click()
    page.locator("//div[@id='city']").click()
    page.locator("//div[text()='Delhi']")
    submit_button = page.get_by_role('button', name='Submit')
    submit_button.click()
