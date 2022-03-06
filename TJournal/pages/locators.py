from selenium.webdriver.common.by import By

class BasePageLocators:
    START_BUTTON = (By.ID, "ru.kraynov.app.tjournal:id/startButton")
    END_BUTTON =  (By.ID, "ru.kraynov.app.tjournal:id/endButton")

class MainPageLocators:
    HEADER = (By.ID, "ru.kraynov.app.tjournal:id/title1")
    POPULARITY_BUTTON =  (By.ID, "ru.kraynov.app.tjournal:id/tabText1")
    EXPAND_POPULARITY_BUTTON =  (By.ID, "ru.kraynov.app.tjournal:id/expandIcon1")
    NEW_BUTTON =  (By.ID, "ru.kraynov.app.tjournal:id/tabText1")
    EXPAND_NEW_BUTTON =  (By.ID, "ru.kraynov.app.tjournal:id/expandIcon2")


