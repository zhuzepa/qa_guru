import pytest
from selenium import webdriver
from selene import browser

@pytest.fixture(scope='session',
                autouse=True)  # scope='function' вызывается для функции, autouse=True чтобы вызывалась автоматически
def browser_management():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs'
    browser.config.timeout = 2.0
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--headless")
    browser.config.driver_options = driver_options

    yield  # передает выполнение тесту

    browser.quit()
