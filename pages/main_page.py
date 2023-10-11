from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self, xpath):
        return super().is_page_loaded(xpath)

    def scroll_to_bottom(self):
        return super().scroll_to_bottom()

    def click_on_element(self, xpath):
        return super().click_on_element(xpath)

    def check_element_is_visible(self, xpath):
        return super().check_element_is_visible(xpath)

