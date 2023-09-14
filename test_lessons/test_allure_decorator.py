import allure
from selene import browser, be, by


def test_decorator_steps(seting_browser):
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_responsitory('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('76')


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('https://github.com')
@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(repo).press_enter()

@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_responsitory(repo):
    browser.element(by.link_text('eroshenkoam/allure-example')).click()

@allure.step('Открываем там Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()

@allure.step('Проверяем наличие Issue с номером {number}')
def should_see_issue_with_number(number):
    browser.element(by.partial_text('#' + number)).should(be.visible).click()
