import pytest
import allure
import time
from TJournal.pages.base_page import BasePage
from TJournal.pages.main_page import MainPage

class TestMainPage:
    def test_is_main_page_opened(self, driver_mobile):
        page = BasePage(driver_mobile)
        page.start_app()
        page = MainPage(driver_mobile)
        page.is_main_page_header_appeared()
