import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    yield page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    yield page
