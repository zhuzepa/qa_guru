import pytest
from selene import browser


@pytest.fixture
def browser_size():
    # выполнение перед тестом
    browser.config.window_width = 2000
    browser.config.window_height = 1080
    yield


    browser.quit()
