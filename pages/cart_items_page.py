from selenium.webdriver.common.by import By
from python.pages.base_page import Page


class CartItems(Page):
    CART_TEXT = (By.XPATH, "//div[contains(@class, 'sc-y')]")

    def cart_items_total(self, expected_result):
        self.verify_partial_text(expected_result, *self.CART_TEXT)