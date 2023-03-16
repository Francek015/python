from selenium.webdriver.common.by import By
from python.pages.base_page import Page


class Verification(Page):
    SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")
    CART_TEXT = (By.XPATH, "//div[contains(@class, 'sc-y')]")
    def signin_verification(self):
        self.verify_partial_text('Sign in', *self.SIGNIN_TEXT)


    def cart_items_total(self):
        self.verify_partial_text('Your Amazon Cart is empty', *self.CART_TEXT)