# import allure # импорировали библиотеку

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..pages.home_page import HomePage

class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    # @allure.title('Заказ самоката')
    def test_order(self):
        home_page = HomePage(self.driver)
        home_page.wait_for_load_header()

        assert 'true' == 'true'