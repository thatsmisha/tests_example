from TJournal.pages.base_page import BasePage
from TJournal.pages.locators import SearchPageLocators
from selenium.webdriver.common.keys import Keys
import time

class SearchPage(BasePage):

    def is_search_page_header_appeared(self):
        header = self.driver.find_element(*SearchPageLocators.HEADER).text
        assert header == 'Обзор', 'Main page has not been opened'

    def input_search_text(self, text):
        search = self.driver.find_element(*SearchPageLocators.SEARCH)
        search.click()
        search.send_keys(text)

    def is_input_text(self, text):
        text_fact = self.driver.find_element(*SearchPageLocators.SEARCH).text
        assert text_fact == text, 'Text is in input field is not as expected. It is: ' + text_fact


