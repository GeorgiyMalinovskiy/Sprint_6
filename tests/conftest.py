import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    
    def slow_down(original_function):
        def wrapper(*args, **kwargs):
            result = original_function(*args, **kwargs)
            time.sleep(1)  # Пауза 1 секунда
            return result
        return wrapper
    
    # Замедляем только поиск элементов
    driver.find_element = slow_down(driver.find_element)
    
    yield driver
    driver.quit() 