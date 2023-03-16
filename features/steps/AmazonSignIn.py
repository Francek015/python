from selenium.webdriver.common.by import By
from behave import given, when, then



@when('Orders clicked')
def click_orders(context):
    context.app.header.click_orders()


@then('Verify {sign_in} page opened')
def signin_verification(context, sign_in):
    context.app.verification_page.signin_verification()

# expected_result = 'Sign in'
# actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
# print(actual_result)
#
# assert expected_result == actual_result
# print('Test phase one passed')
#
# expected_result = ''
# actual_result = driver.find_element(By.ID, "ap_email").text
#
# assert expected_result == actual_result
# print('Test phase two passed')
#
# driver.quit()