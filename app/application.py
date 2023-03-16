from python.pages.main_page import MainPage
from python.pages.header import Header
from python.pages.search_results_page import SearchResultsPage
from python.pages.verification_page import Verification

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.verification_page = Verification(self.driver)
