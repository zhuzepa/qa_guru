from selene.support.shared import browser
from selene import be, have
from selenium import webdriver
import pytest

browser.config.hold_driver_at_exit = True



def test_google_positive(browser_setup):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('первая грузовая компания').press_enter()
    browser.element('[id="search"]').should(have.text('ПГК перевозит грузы как по России, так и за рубежом в пределах колеи 1520. В управлении у оператора находится более 100 тыс. вагонов.'))


def test_google_negative(browser_setup):
     browser.open('https://google.com')
     browser.element('[name="q"]').should(be.blank).type('1йцукенршщсомммывмисмисуукукмпима').press_enter()
     browser.element("//*[@class='v3jTId']").should(have.text('Похоже, по вашему запросу нет полезных результатов'))
