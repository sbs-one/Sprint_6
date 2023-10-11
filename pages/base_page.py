from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def is_page_loaded(self, xpath):
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except NoSuchElementException:
            return False

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_on_element(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.click()
            return True
        except NoSuchElementException:
            return False

    def check_element_is_visible(self, xpath):
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except NoSuchElementException:
            return False

    def send_keys(self, xpath, text):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.send_keys(text)
            return True
        except NoSuchElementException:
            return False



