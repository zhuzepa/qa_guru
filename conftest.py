from selene import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://google.com'
    browser.config.window_width = 2200
    browser.config.window_height = 1080