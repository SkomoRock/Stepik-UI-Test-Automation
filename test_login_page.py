# run command:
# py -m pytest -v --tb=line --language=en test_login_page.py

from pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/accounts/login'

def test_guest_should_see_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
