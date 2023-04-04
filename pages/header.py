from selenium.webdriver.common.by import By
from python.pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
    NAV_ORDERS_BUTTON = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart')
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, 'a[href="#switch-lang=es_US"]')

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

    def verify_lang_shown(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)
        