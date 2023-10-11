from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self, xpath):
        return super().is_page_loaded(xpath)

    def send_keys(self, xpath, text):
        return super().send_keys(xpath, text)

    def click_on_element(self, xpath):
        return super().click_on_element(xpath)

    def check_url(self, expected_url):
        return super().wait_for_url_to_match(expected_url)
