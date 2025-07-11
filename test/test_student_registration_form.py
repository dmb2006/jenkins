import allure
from demoga_test.data.users import User
from demoga_test.enum.enum import Gender, Hobbies, State
from demoga_test.page.registaration_page import RegistrationPage
from allure_commons.types import Severity



@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'mininAV')
@allure.feature('Успешная регистрация пользователя')
@allure.link('https://demoqa.com/automation-practice-form', name="demoqa.com")
@allure.story('ST-001')
def test_student_registration_form(setup_browser):
    with allure.step('Открытие страницы для тестирования'):
        registration_page = RegistrationPage()

    student = User(
        first_name='Alex',
        last_name='Potapov',
        email='potap@ya.ru',
        gender=Gender.MALE.value,
        mobile='0123456789',
        year='1986',
        month='August',
        day='12',
        subject='Computer Science',
        hobbies=Hobbies.MUSIC.value,
        picture_name='cbr600rr.jpeg',
        address='Saint-Petersburg Nevskiy street',
        state=State.NCR.value,
        city='Noida'
    )

    with allure.step('Заполнение формы тестовыми данными'):
        registration_page.full_fill_registration_form(student)

    with allure.step('Проверка, что данные совпадают'):
        registration_page.should_registration_fill_form(student)
