from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    yield chrome_driver


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    language_field = Select(driver.find_element(By.XPATH, "//select[@class='form-select']"))
    language_field.select_by_value('3')
    submit_button = driver.find_element(By.XPATH, "//input[@id='submit-id-submit']")
    submit_button.click()


def test_press_start_button(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_button.click()
    wait = WebDriverWait(driver, 60)
    hello_world_locator = ("xpath", "//div[@id='finish']")
    hello_word_element = wait.until(EC.visibility_of_element_located(hello_world_locator))
    check_hello_word = driver.find_element(By.XPATH, "//div[@id='finish']/h4")
    assert check_hello_word.text == "Hello World!"
