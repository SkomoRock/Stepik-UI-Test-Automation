import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):

    def add_product_to_basket(self):
        try:
            button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
            button.click()
        except: assert False, 'Button add to basket is NOT PRESENTED'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')
