from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_add_item_on_cart(driver):
    driver.get('https://www.demoblaze.com/index.html')
    item_name = "Sony vaio i5"
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, item_name)))
    link = driver.find_element(By.LINK_TEXT, item_name)
    ActionChains(driver).key_down(Keys.COMMAND).click(link).key_up(Keys.COMMAND).perform()
    driver.switch_to.window(driver.window_handles[1])
    add_cart_button = driver.find_element(By.XPATH, "//a[text()='Add to cart']")
    add_cart_button.click()
    sleep(2)
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    cart_button = driver.find_element(By.XPATH, "//a[@id='cartur']")
    cart_button.click()
    assertion_selector = f"//td[text()='{item_name}']"
    driver.find_elements(By.XPATH, assertion_selector)
