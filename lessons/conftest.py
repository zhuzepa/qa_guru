import pytest
from selenium import webdriver
from selene import browser




@pytest.fixture(scope='function',
                autouse=True)  # scope='function' вызывается для функции, autouse=True чтобы вызывалась автоматически
def browser_management():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    driver.set_window_size(1920, 1080)
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_name = 'chrome'
    browser.config.timeout = 6.0
    #browser.config.click_by_js = True

    yield  # передает выполнение тесту

    browser.quit()
