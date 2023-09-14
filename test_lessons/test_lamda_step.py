from selene import browser, be, by
import allure

def test_lamda_step(seting_browser):
    with allure.step('Открытие главной странице'):
        browser.open('/')
    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element('#issues-tab').click()
    with allure.step('Проверяем наличие issue 76'):
        browser.element(by.partial_text('#76')).should(be.visible)
