from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then



@given('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@when('Bestsellers is clicked')
def click_bestsellers(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/Best-Sellers/z')]").click()


@then('Verify 5 links are shown')
def verify_links(context):
    expected_result = 5
    result_length = context.driver.find_elements(By.XPATH, "//div[@id='zg_header']/div/div/div/ul/li")
    # $$('#zg_header a')
    actual_result = len(result_length)
    print(actual_result)
    assert actual_result == expected_result
