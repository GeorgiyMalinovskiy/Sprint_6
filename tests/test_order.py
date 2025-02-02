import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
import allure
from datetime import datetime, timedelta

class TestScooterOrder:
    
    @allure.feature('Заказ самоката')
    @allure.story('Позитивный сценарий заказа')
    @pytest.mark.parametrize('button_position, user_data, rent_data', [
        ('top', {
            'name': 'Иван',
            'surname': 'Иванов',
            'address': 'ул. Ленина, 1',
            'metro': 'Сокольники',
            'phone': '+79991234567'
        }, {
            'date': (datetime.now() + timedelta(days=1)).strftime('%d.%m.%Y'),
            'rental_period': 'сутки',
            'color': 'black',
            'comment': 'Позвоните за час до доставки'
        }),
        ('bottom', {
            'name': 'Петр',
            'surname': 'Петров',
            'address': 'ул. Пушкина, 10',
            'metro': 'Лубянка',
            'phone': '+79997654321'
        }, {
            'date': (datetime.now() + timedelta(days=2)).strftime('%d.%m.%Y'),
            'rental_period': 'двое суток',
            'color': 'grey',
            'comment': 'Домофон не работает, звоните'
        })
    ])
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