from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class OrderPage(BasePage):
    # Локаторы формы заказа
    NAME_INPUT = (By.CSS_SELECTOR, "[placeholder='* Имя']")
    SURNAME_INPUT = (By.CSS_SELECTOR, "[placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "[placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.CSS_SELECTOR, ".select-search__input")
    METRO_STATION_OPTION = (By.CSS_SELECTOR, ".select-search__select .select-search__row")
    PHONE_INPUT = (By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")
    
    # Локаторы второй страницы заказа
    DATE_INPUT = (By.CSS_SELECTOR, "[placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CSS_SELECTOR, ".Dropdown-control")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")
    
    # Локатор подтверждения заказа
    ORDER_CONFIRM = (By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ")
    
    # Локатор кнопки подтверждения в модальном окне
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    def select_metro_station(self, station_name):
        self.click(self.METRO_STATION)
        self.send_keys(self.METRO_STATION, station_name)
        self.wait.until(expected_conditions.presence_of_element_located(self.METRO_STATION_OPTION)).click()

    def fill_order_form(self, user_data):
        self.send_keys(self.NAME_INPUT, user_data["name"])
        self.send_keys(self.SURNAME_INPUT, user_data["surname"])
        self.send_keys(self.ADDRESS_INPUT, user_data["address"])
        self.select_metro_station(user_data["metro"])
        self.send_keys(self.PHONE_INPUT, user_data["phone"])
        self.click(self.NEXT_BUTTON)

    def fill_rent_form(self, rent_data):
        # Вводим дату и нажимаем Enter чтобы закрыть календарь
        self.send_keys(self.DATE_INPUT, rent_data["date"] + Keys.ENTER)
        
        self.click(self.RENTAL_PERIOD)
        rental_option = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{rent_data['rental_period']}']")
        self.wait.until(expected_conditions.presence_of_element_located(rental_option)).click()
        
        if rent_data["color"] == "black":
            self.click(self.COLOR_BLACK)
        elif rent_data["color"] == "grey":
            self.click(self.COLOR_GREY)
            
        if "comment" in rent_data:
            self.send_keys(self.COMMENT_INPUT, rent_data["comment"])
            
        self.click(self.ORDER_BUTTON)
        # Подтверждаем заказ в модальном окне
        self.click(self.CONFIRM_BUTTON)
