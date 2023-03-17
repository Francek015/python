from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep

SELECTION_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_OPTION = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_number} page')
def open_product_page(context, product_number):
    context.driver.get(f'https://www.amazon.com/dp/{product_number}/')
    sleep(1)


@then('Verify user can select each option')
def verify_user_can_select_options(context):
    context.driver.find_element(*SELECTION_OPTIONS).click()
    sleep(1)

    all_selections = context.driver.find_elements(*SELECTION_OPTIONS)
    print(f'all selections: {all_selections}')
    expected_result = ['Apricot', 'Dustyblue', 'Khaki', 'Offwhite', 'Peagreen']

    actual_selected = []
    for item in all_selections[:6]:
        item.click()
        current_color = context.driver.find_element(*CURRENT_OPTION).text
        print(f'current color: {current_color}')
        actual_selected += [current_color]
    assert expected_result == actual_selected, f'Expected {expected_result}, but got {actual_selected}'



