from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET = (By.CSS_SELECTOR, ".btn-group>a")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_SUBMIT_BUTTON = (By.NAME, "login_submit")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main  .price_color")
    SUCCESSFUL_ALERT = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert  p strong")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(),'Your basket is empty')]")