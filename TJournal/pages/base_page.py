from TJournal.pages.locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver_mobile, timeout=1):  # constructor - initiating when the object is created
        self.driver = driver_mobile
        self.driver.implicitly_wait(timeout)

    # --------------- Start ------------------

    def start_app(self):
        self.wait_for_element_appear(*BasePageLocators.START_BUTTON, timeout=5)
        self.driver.find_element(*BasePageLocators.START_BUTTON).click()  # click on the first start button
        self.wait_for_element_appear(*BasePageLocators.END_BUTTON, timeout=5)
        self.driver.find_element(*BasePageLocators.END_BUTTON).click()  # click on the second start button

    # ------------- Go to --------------------

    def go_to_main_page(self):
        self.driver.find_element(*BasePageLocators.MAIN_PAGE_BUTTON).click()

    def go_to_search_page(self):
        self.driver.find_element(*BasePageLocators.SEARCH_PAGE_BUTTON).click()

    def go_to_add_page(self):
        self.driver.find_element(*BasePageLocators.ADD_PAGE_BUTTON).click()

    # ---------------- Wait for element appearance/disappearance/enable ------------------

    def wait_for_element_appear(self, how, what, timeout=40):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))

    def wait_for_element_disappear(self, how, what, timeout=40):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((how, what)))

    # ---------------- Is element ------------------

    def is_element_located(self, how, what, timeout=4):  # if element is visibe and in a DOM
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_not_located(self, how, what, timeout=4):  # if element is not visibe and in a DOM
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_enabled(self, how, what):  # WORKS only if an element has DISABLED attribute!
        attr = self.driver.find_element(how, what).is_enabled()
        if attr == True:
            return True
        else:
            return False

    def is_element_disabled(self, how, what):  # WORKS only if an element has DISABLED attribute!
        attr = self.driver.find_element(how, what).is_enabled()
        if attr == True:
            return False
        else:
            return True




