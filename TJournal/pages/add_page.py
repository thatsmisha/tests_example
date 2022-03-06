from TJournal.pages.base_page import BasePage
from TJournal.pages.locators import AddPageLocators
import time

class AddPage(BasePage):

    def is_add_page_header_appeared(self):
        header = self.driver.find_element(*AddPageLocators.HEADER).text
        assert header == 'Дополнительно', 'Add page has not been opened'


