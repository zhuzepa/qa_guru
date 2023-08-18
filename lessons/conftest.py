import pytest
from selenium import webdriver
from selene import browser

'''
@pytest.fixture
def browser_setup():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    browser.open('https://google.com')
    driver.set_window_size(2000, 600)

    yield

    browser.close()


@pytest.fixture(scope='session',
                autouse=True)  # scope='function' вызывается для функции, autouse=True чтобы вызывалась автоматически
def browser_management():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs'
    # browser.config.driver_name = 'chrome'
    browser.config.timeout = 2.0
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--headless")
    browser.config.driver_options = driver_options

    yield  # передает выполнение тесту

    browser.quit()
'''

@pytest.fixture()
def demoqa():
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--headless")
    browser.config.driver_options = driver_options