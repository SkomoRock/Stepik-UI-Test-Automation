from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is NOT PRESENTED'

    def go_to_login_page(self):
        try:
            link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
            link.click()
        except:
            assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Go to login page is FAILED'
