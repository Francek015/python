from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')

@given('Open Amazons page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(2)

@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(1)

@when('open Video Games page')
def click_keyboards(context):
    context.driver.find_element(By.ID, "nav-search-submit-button").click()
    sleep(2)

@when('Click on item')
def click_item(context):
    context.driver.find_element(By.XPATH, "//*[contains(@aria-label,'Choice')]").click()
    sleep(2)

@when('Add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button").click()
    sleep(1)

@when('Click go to cart')
def Click_go_to_cart(context):
    context.driver.find_element(By.XPATH, "//*[contains(@href,'/gp/cart/view.html?ref_=sw_gtc')]").click()
    # number = context.driver.find_element(By.ID, "nav-cart-count").text
    # print(number)
    sleep(2)


@then('Verify cart has{user_input} item')
def verify_empty_cart(context, user_input):
    actual_result = int(context.driver.find_element(By.ID, "nav-cart-count").text)
    expected_result = int(user_input)
    # print(type(actual_result))
    # print(type(expected_result))
    assert actual_result == expected_result
