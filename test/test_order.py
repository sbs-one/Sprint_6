from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Pages
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class TestOrder:
    def test_order(self, main_page, order_page, driver):
        assert main_page.is_page_loaded(MainPageLocators.HOME_PAGE_XPATH), "Страница не загрузилась"
        assert main_page.click_on_element(MainPageLocators.FIRST_ORDER_BUTTON), "Кнопка не найдена"
        assert order_page.is_page_loaded(OrderPageLocators.ORDER_PAGE_XPATH), "Страница не загрузилась"
        assert order_page.send_keys(OrderPageLocators.NAME_INPUT, "Степан"), "Ввести имя не удалось"
        assert order_page.send_keys(OrderPageLocators.LASTNAME_INPUT, "Шалагин"), "Ввести фамилию не удалось"
        assert order_page.send_keys(OrderPageLocators.ADDRESS_INPUT, "Бабушкиная 12, кв 1"), "Ввести адрес не удалось"
        assert order_page.click_on_element(OrderPageLocators.NAME_INPUT), "Не удалось нажать на инпут"
        assert order_page.send_keys(OrderPageLocators.METRO_INPUT, "Бабу"), "Ввести метро не удалось"
        assert order_page.click_on_element(OrderPageLocators.METRO_BABUSHKINSKY), "Найти метро не удалось"
        assert order_page.send_keys(OrderPageLocators.PHONE_INPUT, "+79246616896"), "Ввести телефон не удалось"
        assert order_page.click_on_element(OrderPageLocators.NEXT_BUTTON), "Нажать на кнопку Далее - не удалось"
        assert order_page.is_page_loaded(OrderPageLocators.ARENDA_PAGE),"Страница не загрузилась"
        assert order_page.click_on_element(OrderPageLocators.DATE_PICKER), "Нажать на дату не удалось"
        assert order_page.click_on_element(OrderPageLocators.TODAY_DATE)
        assert order_page.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        assert order_page.click_on_element(OrderPageLocators.ONE_DAY)
        assert order_page.click_on_element(OrderPageLocators.COLOR_CHECK_BOX_ONE)
        assert order_page.send_keys(OrderPageLocators.DELIVERY_INSTRUCTION, "У первого подъезда")
        assert order_page.click_on_element(OrderPageLocators.BUTTON_ORDER)
        assert order_page.is_page_loaded(OrderPageLocators.MODAL_WINDOW)
        assert order_page.click_on_element(OrderPageLocators.BUTTON_YES)
        assert order_page.check_element_is_visible(OrderPageLocators.ORDER_FINALIZED)
        assert order_page.click_on_element(OrderPageLocators.BUTTON_CHECK_STATUS)
        assert order_page.click_on_element(OrderPageLocators.SCOOTER_LOGO)
        current_url = driver.current_url  # Corrected line
        assert current_url == Pages.main_page_url, "URL doesn't match the expected URL."
        assert order_page.click_on_element(OrderPageLocators.YANDEX_LOGO)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//button[text()="Найти"]')))
        current_url = driver.current_url  # Corrected line
        assert current_url == Pages.yandex_url, "URL doesn't match the expected URL."





