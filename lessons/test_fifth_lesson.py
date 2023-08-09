from selene import browser, be, have, command
import os
from selenium.webdriver import Keys

browser.config.hold_driver_at_exit = True


def test_fifth_lesson():
    browser.open('/')
    browser.element('img[href=https://demoqa.com/')
    browser.element('img[src="/images/Toolsqa.jpg"]').should(be.visible)
    browser.element('.main-header').should(have.text('Practice Form'))
    browser.element('div.practice-form-wrapper h5').should(have.text('Student Registration Form'))
    browser.element('#firstName').should(have.attribute('placeholder').value('First Name'))
    browser.element('#lastName').should(have.attribute('placeholder').value('Last Name'))
    browser.element('#userEmail').should(have.attribute('placeholder').value('name@example.com'))
    browser.all('input[name="gender"]').should(have.size(3))
    browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number'))
    browser.element('label[for=hobbies-checkbox-1]').should(have.text('Sports'))
    browser.element('label[for=hobbies-checkbox-2]').should(have.text('Reading'))
    browser.element('label[for=hobbies-checkbox-3]').should(have.text('Music'))
    browser.element('#subjectsInput').should(be.blank)

    browser.element('#firstName').type('Ezekiel')
    browser.element('#lastName').type('Romaguera')
    browser.element('#userEmail').type('fakedata72553@gmail.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('label[for="gender-radio-3"]').click()
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__day--031').click()
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
    browser.element('#submit').should(have.css_property("cursor", "pointer"))
    browser.element('#submit').press_enter()
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
