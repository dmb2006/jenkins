from selene import browser, have
import allure
from allure_commons.types import Severity
from demoga_test.data.users import User
from demoga_test.enum.enum import Hobbies, Gender
from demoga_test.pages.resources import path



class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.mobile = browser.element('#userNumber')
        self.dateOfBirthInput = browser.element('#dateOfBirthInput')
        self.year = browser.element('.react-datepicker__year-select')
        self.month = browser.element('.react-datepicker__month-select')
        self.subject = browser.element('#subjectsInput')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.choosing_state = browser.element('[id=state]')
        self.state = browser.all('[id^=react-select][id*=option]')
        self.choosing_city = browser.element('[id=city]')
        self.city = browser.all('[id^=react-select][id*=option]')
        self.submit_button = browser.element('[id=submit]')
        self.greeting_registration = browser.element('[id^=example-modal][id*=title]')
        self.should_registration = browser.element('.table-responsive').all('td')

    def full_fill_registration_form(self, user: User):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.element_by(have.value(user.gender)).element('..').click()
        self.mobile.send_keys(user.mobile)
        self.dateOfBirthInput.click()
        self.year.type(user.year).click()
        self.month.type(user.month).click()
        browser.element(f'.react-datepicker__day--0{user.day}').click()
        self.subject.type(user.subject).press_enter()
        browser.all('.custom-control.custom-checkbox label').element_by(have.text(user.hobbies)).click()
        self.picture.set_value(path(user.picture_name))
        self.address.type(user.address)
        self.choosing_state.click()
        self.state.element_by(have.exact_text(user.state)).click()
        self.choosing_city.click()
        self.city.element_by(have.text(user.city)).click()
        self.submit_button.click()

    def should_registration_fill_form(self, user: User):
        self.greeting_registration.should(have.text('Thanks for submitting the form'))
        self.should_registration.even.should(
            have.exact_texts(f'{user.first_name} {user.last_name}', user.email, user.gender, user.mobile,
                       f'{user.day} {user.month},{user.year}', user.subject, user.hobbies, user.picture_name,
                       user.address, f'{user.state} {user.city}'))
