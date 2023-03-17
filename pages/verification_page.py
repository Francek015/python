from selenium.webdriver.common.by import By
from python.pages.base_page import Page


class Verification(Page):
    SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")
    CART_TEXT = (By.XPATH, "//div[contains(@class, 'sc-y')]")

    def signin_verification(self):
        self.verify_partial_text('Sign in', *self.SIGNIN_TEXT)

    def cart_items_total(self, expected_result):
        self.verify_partial_text(expected_result, *self.CART_TEXT)
