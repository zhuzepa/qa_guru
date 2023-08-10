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
    random_year = random.randint(1900, 2101)
    random_year_str = str(random_year)
    browser.all('.react-datepicker__year-select>option').element_by(have.exact_text(random_year_str)).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').send_keys(Keys.ARROW_UP).press_enter()
    random_day = random.randint(1, 30)
    random_day_str = str(random_day)
    browser.all('.react-datepicker__day').element_by(have.exact_text(random_day_str)).click()
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
    browser.element('.table-responsive').should(have.text('Ezekiel Romaguera' and
                                                          'fakedata72553@gmail.com'
                                                          and 'Male'
                                                          and '1234567890'
                                                          and '31 July,2023'
                                                          and 'English, Arts'
                                                          and 'Sports, Reading, Music'
                                                          and 'test_img.jpg'
                                                          and '841 Alvis Union'
                                                          and 'Rajasthan Jaipur'))
    browser.element('#closeLargeModal').click()
