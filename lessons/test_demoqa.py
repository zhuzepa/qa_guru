from selene.support.shared import browser
from selene import be, have

browser.config.hold_driver_at_exit = True

def test_valid_login():
    browser.open('https://demoqa.com/text-box')
    browser.element("//img[@src='/images/Toolsqa.jpg']").should(be.visible)
    browser.element("//*[contains(@class, 'main-header')]").should(have.text('Text Box'))
    browser.element("//*[@id='userName']").type('Rosalind Arusha Arkadina Altalune Florence Thurman-Busson').press_tab()
    browser.element("//*[@id='userEmail']").type('email@123.123.123.123').press_tab()
    browser.element("//*[@id='currentAddress']").type('285 Runte River').press_tab()
    browser.element("//*[@id='permanentAddress']").type('Tamiami 5994 Lon Spur')
    browser.element("//*[@id='submit']").click()

