from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()



driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
print(actual_result)

assert expected_result == actual_result
print('Test phase one passed')

expected_result = ''
actual_result = driver.find_element(By.ID, "ap_email").text

assert expected_result == actual_result
print('Test phase two passed')

driver.quit()