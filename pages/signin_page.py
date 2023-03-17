from selenium.webdriver.common.by import By
from python.pages.base_page import Page


class Signin(Page):
    SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

    def signin_verification(self):
        self.verify_partial_text('Sign in', *self.SIGNIN_TEXT)
