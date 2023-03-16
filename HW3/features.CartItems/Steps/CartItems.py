from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazons page')
def open_google(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Click cart icon')
def click_cart(context):
    context.app.header.click_cart()


@then('Verify {expected_result} is visible')
def verify_empty_cart(context, expected_result):
    # actual_result = context.driver.find_element(By.XPATH, "//div[contains(@class, 'sc-y')]").text
    # assert actual_result == expected_result
    context.app.verification_page.cart_items_total()
