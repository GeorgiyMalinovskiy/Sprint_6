from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage

class HomePage(BasePage):
    # Локаторы для кнопок заказа
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, ".Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")
    
    # Локаторы для логотипов
    SCOOTER_LOGO = (By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI")
    
    # Локаторы для вопросов о важном
    ACCORDION_BUTTONS = (By.CSS_SELECTOR, ".accordion__button")
    ACCORDION_PANELS = (By.CSS_SELECTOR, ".accordion__panel")
    
    # Добавляем локатор для кнопки принятия cookie
    COOKIE_ACCEPT = (By.ID, "rcc-confirm-button")
    
    # Словарь с текстами вопросов и ответов
    FAQ_TEXTS = {
        0: {
            'question': 'Сколько это стоит? И как оплатить?',
            'answer': 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        },
        1: {
            'question': 'Хочу сразу несколько самокатов! Так можно?',
            'answer': 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        },
        2: {
            'question': 'Как рассчитывается время аренды?',
            'answer': 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        },
        3: {
            'question': 'Можно ли заказать самокат прямо на сегодня?',
            'answer': 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        },
        4: {
            'question': 'Можно ли продлить заказ или вернуть самокат раньше?',
            'answer': 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        },
        5: {
            'question': 'Вы привозите зарядку вместе с самокатом?',
            'answer': 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        },
        6: {
            'question': 'Можно ли отменить заказ?',
            'answer': 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        },
        7: {
            'question': 'Я жизу за МКАДом, привезёте?',
            'answer': 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        }
    }

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_load_header(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.ORDER_BUTTON_TOP)
        )

    def click_order_button(self, position="top"):
        if position.lower() == "top":
            self.click(self.ORDER_BUTTON_TOP)
        else:
            self.click(self.ORDER_BUTTON_BOTTOM)
    
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
    
    def get_faq_item(self, index):
        buttons = self.driver.find_elements(*self.ACCORDION_BUTTONS)
        panels = self.driver.find_elements(*self.ACCORDION_PANELS)
        return buttons[index], panels[index]

    def get_faq_text(self, index):
        button, panel = self.get_faq_item(index)
        return button.text, panel.text

    def click_faq_item(self, index):
        button, _ = self.get_faq_item(index)
        button.click()

    def accept_cookies(self):
        """Принимаем cookies"""
        self.click(self.COOKIE_ACCEPT)