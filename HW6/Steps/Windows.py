from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep

PRIVACY_NOTICE_TEXT = (By.XPATH, "//h1[contains(text(),'Privacy Notice')]")


@given('Open amazon T&C page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref'
                       '=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


@when('Store original windows')
def store_original_window(context):
    original_window = context.driver.current_window_handle
    old_windows = context.driver.window_handles
    print(original_window)
    sleep(2)


@when('Click amazon privacy notice')
def click_privacy_notice(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href,'www.amazon.com/p')]").click()
    sleep(2)


@when('Switch to new window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened(current_handles=()))
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)
    print(new_window)
    sleep(2)


@then('Verify amazon privacy notice window opened')
def verify_privacy_notice_window_opened(context):
    context.driver.wait.until(EC.visibility_of_element_located(PRIVACY_NOTICE_TEXT), message='Privacy notice did '
                                                                                              'not appear')


@then('Close window and switch back to original')
def close_and_switch_back_to_original_window(context):
    context.driver.close()
    first_window = context.driver.window_handles[0]
    print(first_window)
    context.driver.switch_to.window(first_window)

