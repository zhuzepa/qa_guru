from selene.support.shared import browser
from selene import be, have



def test_valid_login(demoqa):
    browser.open('/text-box')
    browser.element("a[href='https://demoqa.com']").should(be.visible)
    browser.element(".main-header").should(have.text('Text Box'))
    browser.element("#userName").type('Rosalind Arusha Arkadina Altalune Florence Thurman-Busson').press_tab()
    browser.element("#userEmail").type('email@123.123.123.123').press_tab()
    browser.element("#currentAddress").type('285 Runte River').press_tab()
    browser.element("#permanentAddress").type('Tamiami 5994 Lon Spur').press_tab()
    browser.element("#submit").click()

