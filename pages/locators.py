from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'id_login-username')
    LOGIN_PASSWORD = (By.ID, 'id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login_form .btn.btn-lg.btn-primary')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD1 = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '#register_form .btn.btn-lg.btn-primary')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    SUCCESS_ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert-success .alertinner strong')
    INFO_ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, '#messages .alert-info .alertinner p:first-of-type strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p:first-of-type')
