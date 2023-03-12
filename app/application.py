from python.pages.main_page import MainPage
from python.pages.header import Header
class Application:
    def __int__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)

