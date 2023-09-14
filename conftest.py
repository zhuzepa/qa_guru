from selene import browser, have, be
import pytest

@pytest.fixture
def seting_browser():
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1082

    yield