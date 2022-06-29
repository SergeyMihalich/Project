from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD_1 = (By.ID, 'id_registration-password1')
    PASSWORD_2 = (By.ID, 'id_registration-password2')
    REG_BUTTON = (By.CSS_SELECTOR, '#id_registration-redirect_url~button')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REG_FORM = (By.ID, 'register_form')


class ProductLocators():
    PRODUCT_LINK = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    SHOPPING_CART = (By.XPATH, '//*[@id="messages"]/div[1]//strong')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_IN_CART = (By.XPATH, '//*[@id="messages"]//p/strong')
    PRICE_IN_PRODUCT = (By.CSS_SELECTOR, '.product_main p.price_color')

class OpenBasket():
    BASKET = (By.CSS_SELECTOR, 'span.btn-group a')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    MESSAGE_IN_BASKET = (By.CSS_SELECTOR, '#content_inner p')