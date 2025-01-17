from selenium.webdriver.common.by import By
from python.pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
    NAV_ORDERS_BUTTON = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart')
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, 'a[href="#switch-lang=es_US"]')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    ACCOUNT_OPTIONS = (By.ID, 'nav-link-accountList')
    LIST_OPTION = (By.ID, 'nav-al-title')

    def input_search_text(self, text):
        self.input_text(text, *self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_SUBMIT)

    def click_orders(self):
        self.click(*self.NAV_ORDERS_BUTTON)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def hover_lang_options(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def hover_account_options(self):
        account_options = self.find_element(*self.ACCOUNT_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(account_options)
        actions.perform()

    def select_department(self, alias):
        department_dd = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dd)
        select.select_by_value(f'search-alias={alias}')

    def verify_lang_shown(self):
        self.find_element(*self.SPANISH_LANG)
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def verify_option_shown(self):
        self.find_element(*self.LIST_OPTION)
        self.wait_for_element_appear(*self.LIST_OPTION)
