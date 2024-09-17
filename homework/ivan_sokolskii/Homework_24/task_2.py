from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_hover(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    target_element = driver.find_element(By.XPATH, "//img[@alt='Push It Messenger Bag']")
    add_to_compare_button = driver.find_element(By.XPATH, "//a[@title='Add to Compare']")
    action = ActionChains(driver)
    action.move_to_element(target_element)
    action.move_to_element(add_to_compare_button)
    action.click(add_to_compare_button)
    action.perform()
    compare_count = driver.find_element(By.XPATH, "//span[@class='counter qty']").text
    assert compare_count == "1 item"
