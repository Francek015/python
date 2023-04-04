from python.pages.main_page import MainPage
from python.pages.header import Header
from python.pages.search_results_page import SearchResultsPage
from python.pages.signin_page import Signin
from python.pages.cart_items_page import CartItems
from python.pages.base_page import Page


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.signin_page = Signin(self.driver)
        self.cart_items_page = CartItems(self.driver)
        self.base_page = Page(self.driver)
