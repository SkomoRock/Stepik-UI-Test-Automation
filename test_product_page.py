# run command:
# py -m pytest -v --tb=line --language=en test_product_page.py
# py -m pytest -v --tb=line --language=en -m need_review

import time
import pytest
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_checking()
    page.basket_cost_checking()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_order_button()
    page.should_be_continue_link()

# self argument must be present first
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope = 'function', autouse = True)
    def setup(self, browser):
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time()) + 'fakeword'
        link = 'http://selenium1py.pythonanywhere.com/accounts/login'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.product_name_checking()
        page.basket_cost_checking()
