import pytest
import allure
from TJournal.pages.base_page import BasePage
from TJournal.pages.main_page import MainPage
from TJournal.pages.search_page import SearchPage
from TJournal.pages.add_page import AddPage

@pytest.mark.TestMainPage
class TestMainPage:

    @pytest.mark.mobile
    @allure.feature('MainPage')
    @allure.story('Check - Main page has been opened')
    @allure.severity('Blocker')
    def test_is_main_page_opened(self, driver_mobile):
        page = BasePage(driver_mobile)
        page.start_app()
        page = MainPage(driver_mobile)
        page.is_main_page_header_appeared()  # Check

    @pytest.mark.mobile
    @allure.feature('MainPage')
    @allure.story('Check - Main page has been opened after add page')
    @allure.severity('High')
    def test_is_main_page_opened_after_add(self, driver_mobile):
        page = BasePage(driver_mobile)
        page.start_app()
        page.go_to_add_page()
        page.go_to_main_page()
        page = MainPage(driver_mobile)
        page.is_main_page_header_appeared()  # Check

@pytest.mark.TestAddPage
class TestAddPage:

    @pytest.mark.mobile
    @allure.feature('AddPage')
    @allure.story('Check - Add page has been opened')
    @allure.severity('Blocker')
    def test_is_add_page_opened(self, driver_mobile):
        page = BasePage(driver_mobile)
        page.start_app()
        page.go_to_add_page()
        page = AddPage(driver_mobile)
        page.is_add_page_header_appeared()  # Check

@pytest.mark.TestSearchPage
class TestSearchPage:

    @pytest.mark.mobile
    @allure.feature('SearchPage')
    @allure.story('Check - Search page has been opened')
    @allure.severity('Blocker')
    def test_is_search_page_opened(self, driver_mobile):
        page = BasePage(driver_mobile)
        page.start_app()
        page.go_to_search_page()
        page = SearchPage(driver_mobile)
        page.is_search_page_header_appeared()  # Check

    @pytest.mark.mobile
    @allure.feature('SearchPage')
    @allure.story('Check - Input text is in the field')
    @allure.severity('High')
    def test_is_text_input(self, driver_mobile):
        page = BasePage(driver_mobile)
        page.start_app()
        page.go_to_search_page()
        page = SearchPage(driver_mobile)
        page.input_search_text('Тест')
        page.is_input_text('Тест')  # Check




