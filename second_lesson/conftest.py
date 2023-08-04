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
