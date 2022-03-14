# run command:
# py -m pytest -v -s --tb=line --language=en test_product_page.py

from pages.product_page import ProductPage

product_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
