from selene.support.shared import browser
from selene import have, be


def test_google():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('пгк').press_enter()  # should(be.blank) - проверяет, что поле пустое, затем печатает текст и нажимает enter
    browser.element('[id="search"]').should(have.text(
        'ПГК перевозит грузы как по России, так и за рубежом в пределах колеи 1520.'))  # should == assert, have == иметь, text == какой-то текст


def test_invali_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').type('jgkhgjkhgjhgjhghjgbjhgjhgbhjgh').press_enter()
    browser.element('[id="result-stats"]').should(have.text("Результатов: примерно 0"))
