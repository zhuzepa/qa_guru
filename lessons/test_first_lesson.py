from selene.support.shared import browser
from selene import be, have


def test_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('пгк').press_enter()
    browser.element('[id="search"]').should(have.text(
        'ПГК оказывает комплексные услуги по экспедированию грузов как внутри России, так и за рубежом в пределах колеи 1520.'))
