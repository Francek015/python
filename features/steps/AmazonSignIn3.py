from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')

@when('Click Orders into search field')
def click_order(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('Verify {expected_result} is shown')
def verify_prompt(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result
    print(expected_result)


@then('verify input field shown')
def verify_input(context):
    actual_result = context.driver.find_element(By.ID, "ap_email").text
    expected_result = ''
    assert actual_result == expected_result






