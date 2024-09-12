from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.qa-practice.com/elements/input/simple')
input_text = 'kykykyky'
text_string = driver.find_element(By.XPATH, "//input[@id='id_text_string']")
text_string.send_keys(input_text)
text_string.submit()
result_text = driver.find_element(By.XPATH, "//p[@id='result-text']")
assert result_text.text == input_text
print(result_text.text)
