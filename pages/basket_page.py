from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_order_button(self):
        assert self.is_not_element_present(*BasketPageLocators.ORDER_BUTTON), \
            'Order button is PRESENTED, but should NOT BE'

    def should_be_continue_link(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING), \
            'Continue shopping link NOT FOUND'
