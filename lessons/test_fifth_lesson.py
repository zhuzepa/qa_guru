from selene import browser, be, have, command



browser.config.hold_driver_at_exit = True
def test_fifth_lesson():
    browser.open('/')
    browser.element('#firstName').should(have.attribute('placeholder').value('First Name'))
    browser.element('#lastName').should(have.attribute('placeholder').value('Last Name'))
    browser.element('#userEmail').should(have.attribute('placeholder').value('name@example.com'))


    browser.element('#firstName').type('Александр')
    browser.element('#lastName').type('Сергеевич')
    browser.element('#userEmail').type('pushkin@natomsvete.net')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('label[for="gender-radio-3"]').click()
    browser.element('label[for="gender-radio-1"]').click()
    browser.all('input[name="gender"]').should(have.size(3))
    browser.element('#submit').should(have.css_property("cursor", "pointer"))





'''
    browser.element('#new-todo').should(be.blank)

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.size(3))

    #browser.element('#new-todo').perform(command.js.click)
    #save = browser.element('#new-todo').with_(click_by_js=True)
    #save.click()
    #save.click()
    #save.click()
    #save.click()
    '''
