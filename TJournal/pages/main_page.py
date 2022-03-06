from TJournal.pages.base_page import BasePage
from TJournal.pages.locators import MainPageLocators
import time

class MainPage(BasePage):

    def is_main_page_header_appeared(self):
        header = self.driver.find_element(*MainPageLocators.HEADER).text
        assert header == 'Лента', 'Main page has not been opened'


