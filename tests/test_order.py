import pytest
import allure

from pages.home_page import HomePage
from pages.order_page import OrderPage
from tests.data import test_data
class TestScooterOrder:
    
    @allure.feature('Заказ самоката')
    @allure.story('Позитивный сценарий заказа')
    @pytest.mark.parametrize('button_position, user_data, rent_data', test_data)
    def test_order_flow(self, driver, button_position, user_data, rent_data):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        
        # Принимаем cookies перед взаимодействием со страницей
        home_page.accept_cookies()
        
        home_page.click_order_button(button_position)
        order_page.fill_order_form(user_data)
        order_page.fill_rent_form(rent_data)
        
        # Проверяем, что появилось окно с подтверждением заказа
        assert order_page.is_element_visible(order_page.ORDER_CONFIRM)