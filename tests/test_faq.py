import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
import allure

class TestFAQ:
    @allure.feature('FAQ')
    @allure.story('Проверка выпадающего списка вопросов')
    @pytest.mark.parametrize('faq_index', range(8))
    def test_faq_accordion(self, driver, faq_index):
        home_page = HomePage(driver)
        home_page.wait_for_load_header()

        # Проверяем текст вопроса
        button, panel = home_page.get_faq_item(faq_index)
        expected_question = home_page.FAQ_TEXTS[faq_index]['question']
        assert button.text == expected_question, f'Неверный текст вопроса #{faq_index + 1}'
        
        # Проверяем, что панель изначально скрыта
        assert not panel.is_displayed(), f'Панель ответа #{faq_index + 1} отображается до клика'
        
        button.click()
        
        # Проверяем, что панель стала видимой
        assert panel.is_displayed(), f'Панель ответа #{faq_index + 1} не отображается после клика'
        
        # Проверяем текст ответа
        expected_answer = home_page.FAQ_TEXTS[faq_index]['answer']
        assert panel.text == expected_answer, f'Неверный текст ответа #{faq_index + 1}'
        
        # Проверяем, что повторный клик скрывает ответ
        button.click()
        WebDriverWait(driver, 3).until_not(
            expected_conditions.visibility_of(panel)
        )
        assert not panel.is_displayed(), f'Панель ответа #{faq_index + 1} не скрывается после повторного клика'

    @allure.feature('FAQ')
    @allure.story('Проверка одновременного отображения вопросов')
    def test_multiple_faq_items(self, driver):
        home_page = HomePage(driver)
        home_page.wait_for_load_header()
        
        # Открываем первый и последний вопросы
        home_page.click_faq_item(0)
        home_page.click_faq_item(7)
        
        # Проверяем, что оба ответа видны
        _, panel1 = home_page.get_faq_item(0)
        _, panel2 = home_page.get_faq_item(7)
        
        assert panel1.is_displayed(), 'Первый ответ не отображается'
        assert panel2.is_displayed(), 'Последний ответ не отображается' 