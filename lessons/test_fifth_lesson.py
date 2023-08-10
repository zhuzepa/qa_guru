import random

from selene import browser, be, have, command
import os
from selenium.webdriver import Keys


def test_fifth_lesson():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Ezekiel')
    browser.element('#lastName').type('Romaguera')
    browser.element('#userEmail').type('fakedata72553@gmail.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('label[for="gender-radio-3"]').click()
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select>option[value="1905"]').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__month-select>option[value="11"]').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__day--014').perform(command.js.click)
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('label[for=hobbies-checkbox-1]').perform(command.js.click)
    browser.element('label[for=hobbies-checkbox-2]').perform(command.js.click)
    browser.element('label[for=hobbies-checkbox-3]').perform(command.js.click)
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/test_img.jpg'))
    browser.element('#currentAddress').type('841 Alvis Union')
    browser.element('#state').click()
    browser.element('#react-select-3-input').send_keys(Keys.ARROW_DOWN)
    browser.element('#react-select-3-input').send_keys(Keys.ARROW_DOWN)
    browser.element('#react-select-3-input').send_keys(Keys.ARROW_DOWN).press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').send_keys(Keys.ARROW_UP)
    browser.element('#react-select-4-input').send_keys(Keys.ARROW_UP).press_enter()
    browser.element('#submit').press_enter()
    browser.element('.table-responsive').should(have.text('Ezekiel Romaguera'))
    browser.element('.table-responsive').should(have.text('fakedata72553@gmail.com'))
    browser.element('.table-responsive').should(have.text('1234567890'))
    browser.element('.table-responsive').should(have.text('14 December,1905'))
    browser.element('.table-responsive').should(have.text('English, Arts'))
    browser.element('.table-responsive').should(have.text('Sports, Reading, Music'))
    browser.element('.table-responsive').should(have.text('test_img.jpg'))
    browser.element('.table-responsive').should(have.text('841 Alvis Union'))
    browser.element('.table-responsive').should(have.text('Rajasthan Jaipur'))
    browser.element('#closeLargeModal').click()

