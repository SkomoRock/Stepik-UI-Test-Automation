from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        assert 'login' in self.browser.current_url, \
            'Login page URL is NOT FOUND'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Login form is NOT FOUND'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Register form is NOT FOUND'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL). \
            send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1). \
            send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2). \
            send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON). \
            click()
