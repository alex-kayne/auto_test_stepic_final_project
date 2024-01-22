from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Login url does not contain 'login'"

    def should_be_login_form(self):
        assert self.browser.find_elements(*LoginPageLocators.LOGIN_EMAIL), 'Login form doesnt contain email field'
        assert self.browser.find_elements(*LoginPageLocators.LOGIN_PASSWORD), 'Login form doesnt contain password field'
        assert self.browser.find_elements(*LoginPageLocators.LOGIN_BUTTON), 'Login form doesnt contain login-button'

    def should_be_register_form(self):
        assert self.browser.find_elements(
            *LoginPageLocators.REGISTRATION_EMAIL), 'Registration form doesnt contain email field'
        assert self.browser.find_elements(
            *LoginPageLocators.REGISTRATION_PASSWORD1), 'Registration form doesnt contain password 1 field'
        assert self.browser.find_elements(
            *LoginPageLocators.REGISTRATION_PASSWORD2), 'Registration form doesnt contain password 2 field'
        assert self.browser.find_elements(
            *LoginPageLocators.REGISTRATION_BUTTON), 'Registration form doesnt contain registration-button'
