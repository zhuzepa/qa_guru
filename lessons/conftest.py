import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture
def browser_setup():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    browser.open('https://google.com')
    driver.set_window_size(2000, 600)

    yield

    browser.close()


@pytest.fixture(scope='function',
                autouse=True)  # scope='function' вызывается для функции, autouse=True чтобы вызывалась автоматически
def browser_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.driver_name = 'chrome'
    browser.config.timeout = 6.0
    # browser.config.click_by_js = True

    # driver_options = webdriver.ChromeOptions()
    # browser.config.driver_options = driver_options
    # driver_options.add_argument("--headless")

    # browser.config.type_by_js = True
    # driver_options = webdriver.ChromeOptions()

    yield  # передает выполнение тесту

    browser.quit()
