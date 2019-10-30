from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")	


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    PRICE_ALERT = (By.CSS_SELECTOR, ".alert-info")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_IN_ALERT = (By.CSS_SELECTOR, ".alert-info strong")