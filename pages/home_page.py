from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    header_order_button = [By.XPATH, "//button[text()='Заказать']"]
    faq_list_container = [By.CLASS_NAME, 'Home_FAQ__3uVm4']

    def __init__(self, driver):
        self.driver = driver

    def click_header_order_button(self, ):
        self.driver.find_element(*self.header_order_button).click()