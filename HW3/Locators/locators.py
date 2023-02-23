from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/ap/register?openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo').click()
# driver.find_element(By.ID, 'ap_customer_name').click()
# driver.find_element(By.ID, 'ap_email').click()
# driver.find_element(By.ID, 'ap_password').click()
# driver.find_element(By.CSS_SELECTOR, '.a-box.a-alert-inline.a-alert-inline-info')
# driver.find_element(By.ID, 'ap_password_check').click()
# driver.find_element(By.ID, 'continue').click()
# driver.find_element(By.XPATH, "//a[contains(@href, 'condition')]").click()
driver.find_element(By.XPATH, "//a[contains(@href, 'register_notification_p')]").click()
