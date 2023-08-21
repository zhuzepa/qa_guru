from selene import browser
import pytest

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://google.com'