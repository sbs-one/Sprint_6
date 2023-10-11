class OrderPageLocators:
    ORDER_PAGE_XPATH = "//div[contains(text(),'Для кого самокат')]"
    NAME_INPUT = '//input[@placeholder="* Имя"]'
    LASTNAME_INPUT = '//input[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_INPUT = '//input[@placeholder="* Станция метро"]'
    METRO_BABUSHKINSKY = '//button[contains(@class, "Order_SelectOption") and div[text()="Бабушкинская"]]'
    PHONE_INPUT = '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = "//button[contains(text(),'Далее')]"
    ARENDA_PAGE = "//div[contains(text(),'Про аренду')]"
    DATE_PICKER = '//input[@placeholder="* Когда привезти самокат"]'
    TODAY_DATE = "//div[contains(@class, 'today')]"
    RENTAL_PERIOD = "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']"
    ONE_DAY = "//div[@class='Dropdown-option' and text()='сутки']"
    COLOR_CHECK_BOX_ONE = "//label[contains(text(), 'чёрный жемчуг')]"
    DELIVERY_INSTRUCTION = '//input[@placeholder="Комментарий для курьера"]'
    BUTTON_ORDER = "//div[starts-with(@class, 'Order_Buttons')]//button[contains(text(), 'Заказать')]"
    MODAL_WINDOW = "//div[contains(text(),'Хотите оформить заказ?')]"
    BUTTON_YES = "//button[contains(text(),'Да')]"
    ORDER_FINALIZED = "//div[contains(text(),'Заказ оформлен')]"
    SCOOTER_LOGO = '//img[@alt="Scooter"]'
    YANDEX_LOGO = '//img[@alt="Yandex"]'
    BUTTON_CHECK_STATUS = '//button[contains(text(),"Посмотреть статус")]'
