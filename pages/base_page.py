import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Клик по элементу {locator}')
    def click(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step('Поиск элемента {locator}')
    def find_element(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Проверка видимости элемента {locator}')
    def is_element_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ввод текста в элемент {locator}')
    def send_keys(self, locator, text):
        self.wait.until(expected_conditions.presence_of_element_located(locator)).send_keys(text)