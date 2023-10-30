from selenium.webdriver.common.by import By


class DropdownLocators:
    BUTTON_CONFIRM = (By.ID, "rcc-confirm-button")
    DROPDOWN_ELEMENT_1 = (By.XPATH, '//div[contains(text(), "Сколько это стоит? И как оплатить?")]')
    DROPDOWN_ELEMENT_2 = (By.XPATH, '//div[contains(text(), "Хочу сразу несколько самокатов! Так можно?")]')
    DROPDOWN_ELEMENT_3 = (By.XPATH, '//div[contains(text(), "Как рассчитывается время аренды?")]')
    DROPDOWN_ELEMENT_4 = (By.XPATH, '//div[contains(text(), "Можно ли заказать самокат прямо на сегодня?")]')
    DROPDOWN_ELEMENT_5 = (By.XPATH, '//div[contains(text(), "Можно ли продлить заказ или вернуть самокат раньше?")]')
    DROPDOWN_ELEMENT_6 = (By.XPATH, '//div[contains(text(), "Вы привозите зарядку вместе с самокатом?")]')
    DROPDOWN_ELEMENT_7 = (By.XPATH, '//div[contains(text(), "Можно ли отменить заказ?")]')
    DROPDOWN_ELEMENT_8 = (By.XPATH, '//div[contains(text(), "Я жизу за МКАДом, привезёте?")]')
    DROPDOWN_TEXT_1 = (By.CSS_SELECTOR, 'div[data-accordion-component="AccordionItemPanel"][id="accordion__panel-0"]')
    DROPDOWN_TEXT_2 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-1'][@id='accordion__panel-1']")
    DROPDOWN_TEXT_3 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-2'][@id='accordion__panel-2']")
    DROPDOWN_TEXT_4 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-3'][@id='accordion__panel-3']")
    DROPDOWN_TEXT_5 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-4'][@id='accordion__panel-4']")
    DROPDOWN_TEXT_6 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-5'][@id='accordion__panel-5']")
    DROPDOWN_TEXT_7 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-6'][@id='accordion__panel-6']")
    DROPDOWN_TEXT_8 = (By.XPATH, "//div[@aria-labelledby='accordion__heading-7'][@id='accordion__panel-7']")


class OrderLocators:
    ORDER_BUTTON_UPPER = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_DOWN = (By.XPATH, '//button[contains(text(), "Заказать")]')
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    CHEKBOX_LOKATOR = (
    By.XPATH, '//button[contains(@class, "Order_SelectOption") and div[text()="Бульвар Рокоссовского"]]')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Далее")]')
    DELIVERY_DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DROPDOWN_ELEMENT = (By.CLASS_NAME, 'Dropdown-control')
    DROPDOWN_MENU_DAY = (
    By.XPATH, '//div[@class="Dropdown-option" and @role="option" and @aria-selected="false" and text()="сутки"]')
    CHECKBOXES_ELEMENT = (By.XPATH, '//input[@id="black" and @class="Checkbox_Input__14A2w" and @type="checkbox"]')
    COURIER_COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_ACCEPT = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')
    YES_BUTTON = (By.XPATH, '//button[contains(text(), "Да")]')
    VIEW_STATUS_FORM = (By.CLASS_NAME, 'Order_Modal__YZ-d3')
    VIEW_STATUS_BUTTON = (By.XPATH, '//button[contains(text(), "Посмотреть статус")]')
    SCOOTER_IMAGE = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]/img[@alt="Scooter"]')
    YANDEX_IMAGE = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")]/img[@alt="Yandex"]')
    TEXT = (By.XPATH, '//div[text()="Про аренду"]')
    BUTTON_CONFIRM = ((By.CSS_SELECTOR, 'button#rcc-confirm-button'))
    DZEN = (By.XPATH, '//div[text()="Новости"]')
