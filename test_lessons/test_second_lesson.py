from selene.support.shared import browser
from selene import be, have


def test_google_positive(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(
        'первая грузовая компания').press_enter()  # should(be.blank) - елемент должен быть пустым, потм ввести текст и нажать enter
    browser.element('[id="search"]').should(have.text(  # должен иметь текст
        'ПГК перевозит грузы как по России, так и за рубежом в пределах колеи 1520.'
        ' В управлении у оператора находится более 100 тыс. вагонов.'))


def test_google_negative(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('1йцукенршщсомммывмисмисуукукмпима24у2424232').press_enter()
    browser.element("//*[@class='v3jTId']").should(have.text('Похоже, по вашему запросу нет полезных результатов'))
