from selenium.webdriver.common.by import By
from python.pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        self.open_url('https://www.amazon.com')


    def open_outlet(self):
        self.open_url('https://www.amazon.com/outlet/?_encoding=UTF8&ref_=sv_subnav_goldbox_3')


    def open_product(self):
        self.open_url('https://www.amazon.com/s?k=watches&ref=nb_sb_noss')
