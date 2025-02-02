import pytest
from selenium import webdriver

@pytest.fixture
def driver(path):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.get(f"https://qa-scooter.praktikum-services.ru/{path}")
    yield driver

    driver.quit()