from selene.support.shared import browser
from selene import be, have

browser.config.hold_driver_at_exit = True

def test_valid_login(browser_setup):
    browser.open('/text-box')
    browser.element("a[href='https://demoqa.com']").should(be.visible)  # проверяем, что элемент отображается
    browser.element(".main-header").should(have.text('Text Box'))  # проверяем, что элемент имеет текст Text Box
    browser.element("#userName").type(
        'Rosalind Arusha Arkadina Altalune Florence Thurman-Busson').press_tab()  # type вводит текст и нажимает tab
    browser.element("#userEmail").type('email@123.123.123.123').press_tab()  # type вводит текст и нажимает tab
    browser.element("#currentAddress").type('285 Runte River').press_tab()  # type вводит текст и нажимает tab
    browser.element("#permanentAddress").type('Tamiami 5994 Lon Spur').press_tab()  # type вводит текст и нажимает tab
    browser.element("#submit").click()  # кликает по кнопке
