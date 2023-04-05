from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Orders clicked')
def click_orders(context):
    context.app.header.click_orders()


@then('Verify {sign_in} page opened')
def signin_verification(context, sign_in):
    context.app.signin_page.signin_verification()


@when('Hover over language options')
def hover_lang_options(context):
    context.app.header.hover_lang_options()


@when('Hover over account')
def hover_account_options(context):
    context.app.header.hover_account_options()


@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)


@then('Verify Spanish option present')
def verify_lang_options_shown(context):
    context.app.header.verify_lang_shown()

@then('Verify Your list is present')
def verify_create_option_shown(context):
    context.app.header.verify_option_shown()



@then('Verify {category} department is selected')
def verify_selected_dept(context, category):
    context.app.search_results_page.verify_selected_dept(category)




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