from selenium.webdriver.common.by import By
from python.pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')
    NAV_ORDERS_BUTTON = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart')

    def input_search_text(self, text):
        self.input_text(text, *self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_SUBMIT)

    def click_orders(self):
        self.click(*self.NAV_ORDERS_BUTTON)

    def click_cart(self):
        self.click(*self.CART_ICON)
