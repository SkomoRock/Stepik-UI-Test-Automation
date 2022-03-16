from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_LINK_INVALID = (By.ID, 'login_link_inc')
    USER_ICON = (By.CLASS_NAME, "icon-user")

class BasketPageLocators():    
    BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    ORDER_BUTTON = (By.ID, 'btn-block')
    CONTINUE_SHOPPING = (By.XPATH, '//*[@id="content_inner"]/p/a')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD_1 = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD_2 = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')

class MainPageLocators():
    LOGIN_LINK = (By.ID, 'login_link')

class ProductPageLocators():
    BUTTON_ADD = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    BASKET_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BASKET_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-success')
