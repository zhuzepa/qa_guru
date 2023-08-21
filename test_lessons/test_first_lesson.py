from selene.support.shared import browser
from selene import be, have


def test_google():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('пгк').press_enter()
    browser.element('[id="search"]').should(have.text(
        'ПГК перевозит грузы как по России, так и за рубежом в пределах колеи 1520. В управлении у оператора находится более 100 тыс. вагонов.'))
