from selenium.webdriver.common.by import By

class BasePageLocators:
    START_BUTTON = (By.ID, "ru.kraynov.app.tjournal:id/startButton")
    END_BUTTON = (By.ID, "ru.kraynov.app.tjournal:id/endButton")
    MAIN_PAGE_BUTTON = (By.XPATH, "//androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup[@index='0']")
    SEARCH_PAGE_BUTTON = (By.XPATH, "//androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup[@index='1']")
    MESSAGES_PAGE_BUTTON = (By.XPATH, "//androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup[@index='2']")
    ALARM_PAGE_BUTTON = (By.XPATH, "//androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup[@index='3']")
    ADD_PAGE_BUTTON = (By.XPATH, "//androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup[@index='4']")

class MainPageLocators:
    HEADER = (By.ID, "ru.kraynov.app.tjournal:id/title1")
    POPULARITY_BUTTON = (By.ID, "ru.kraynov.app.tjournal:id/tabText1")
    EXPAND_POPULARITY_BUTTON = (By.ID, "ru.kraynov.app.tjournal:id/expandIcon1")
    NEW_BUTTON = (By.ID, "ru.kraynov.app.tjournal:id/tabText1")
    EXPAND_NEW_BUTTON = (By.ID, "ru.kraynov.app.tjournal:id/expandIcon2")

class SearchPageLocators:
    HEADER = (By.ID, "ru.kraynov.app.tjournal:id/title1")
    SEARCH = (By.ID, "ru.kraynov.app.tjournal:id/toolbarSearchEditText")

class AddPageLocators:
    HEADER = (By.ID, "ru.kraynov.app.tjournal:id/title1")



