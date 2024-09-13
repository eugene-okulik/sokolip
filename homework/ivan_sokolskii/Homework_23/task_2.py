from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
url = "https://demoqa.com/automation-practice-form"
name = "Ivan"
last_name = "Ivanov"
user_email = "123@ya.ru"
mobile_phone = "1234567891"
dob = '12 Sep 1999'
subjects = "Hello world"
current_address = "Cancun"
driver.get(url)
name_field = driver.find_element(By.XPATH, "//input[@id='firstName']")
name_field.send_keys(name)
last_name_field = driver.find_element(By.XPATH, "//input[@id='lastName']")
last_name_field.send_keys(last_name)
email_field = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email_field.send_keys(user_email)
gender_button = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
gender_button.click()
mobile_phone_field = driver.find_element(By.XPATH, "//input[@id='userNumber']")
mobile_phone_field.send_keys(mobile_phone)
dob_field = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
dob_field.click()
select_year = Select(driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']"))
select_year.select_by_value('1905')
select_mounth = Select(driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']"))
select_mounth.select_by_value('7')
select_day = driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--004']")
select_day.click()
subject_field = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
subject_field.send_keys(subjects)
hobbies_checkbox = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
hobbies_checkbox.click()
current_address_field = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
current_address_field.send_keys(current_address)
choose_state = driver.find_element(By.XPATH, "//div[@class=' css-tlfecz-indicatorContainer']")
choose_state.click()
choose_state_res = driver.find_element(By.XPATH, "//div[text()= 'NCR']")
choose_state_res.click()
choose_city = driver.find_element(By.XPATH, "//div[@id='city']")
choose_city.click()
choose_city_res = driver.find_element(By.XPATH, "//div[text()='Delhi']")
choose_city_res.click()
submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_button.click()
submit_table = driver.find_elements(By.XPATH, '//td')
for element in submit_table:
    print(element.text)
