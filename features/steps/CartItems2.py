from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)
driver.implicitly_wait(4)

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')



# @when('Input {search_word} into search field')
# def input_search(context, search_word):
#     context.driver.wait.until(EC.visibility_of_element_located(SEARCH_INPUT))
#     search = context.driver.find_element(*SEARCH_INPUT)
#     search.clear()
#     search.send_keys(search_word)


@when('open Video Games page')
def click_keyboards(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.ID, "nav-search-submit-button")))
    context.driver.find_element(By.ID, "nav-search-submit-button").click()
    # sleep(2)


@when('Click on item')
def click_item(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@aria-label,'Choice')]")))
    context.driver.find_element(By.XPATH, "//*[contains(@aria-label,'Choice')]").click()
    # sleep(2)


@when('Add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button").click()
    # sleep(1)


@when('Click go to cart')
def Click_go_to_cart(context):
    context.driver.find_element(By.XPATH, "//*[contains(@href,'/gp/cart/view.html?ref_=sw_gtc')]").click()
    # number = context.driver.find_element(By.ID, "nav-cart-count").text
    # print(number)
    # sleep(2)


@then('Verify cart has{user_input} item')
def verify_empty_cart(context, user_input):
    actual_result = int(context.driver.find_element(By.ID, "nav-cart-count").text)
    expected_result = int(user_input)
    # print(type(actual_result))
    # print(type(expected_result))
    assert actual_result == expected_result
