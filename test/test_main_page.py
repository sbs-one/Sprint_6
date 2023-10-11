import pytest

import data
from locators.main_page_locators import MainPageLocators


@pytest.mark.parametrize("question_locator, answer_locator", data.faq_data)
class TestMainPage:
    def test_faq(self, main_page, question_locator, answer_locator):
        assert main_page.is_page_loaded(MainPageLocators.HOME_PAGE_XPATH), "Страница не загрузилась"
        main_page.scroll_to_bottom()
        assert main_page.click_on_element(question_locator), "Вопрос не найден"
        assert main_page.check_element_is_visible(answer_locator), "Ответ не найден"
