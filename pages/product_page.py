import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):

    def add_product_to_basket(self):
        try:
            button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
            button.click()
        except: assert False, 'Button add to basket is NOT FOUND'

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

    def product_name_checking(self):
        expected_result = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        actual_result = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        assert expected_result == actual_result, 'Product name is INCORRECT'

    def basket_cost_checking(self):
        expected_result = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        actual_result = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert expected_result == actual_result, 'Basket cost is INCORRECT'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is PRESENTED, but should NOT BE"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is PRESENTED, but should BE DISAPPEARED"
