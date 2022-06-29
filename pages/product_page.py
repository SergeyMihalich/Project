import math
from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductLocators


class ProductPage(BasePage):
    def product_page(self):
        self.click_button()

    def click_button(self):
        click_but = self.browser.find_element(*ProductLocators.PRODUCT_LINK)
        click_but.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(int(x)))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_buy(self):
        chopping_cart = self.browser.find_element(*ProductLocators.SHOPPING_CART)
        name_producr = self.browser.find_element(*ProductLocators.NAME_PRODUCT)
        price_in_cart = self.browser.find_element(*ProductLocators.PRICE_IN_CART)
        price_in_product = self.browser.find_element(*ProductLocators.PRICE_IN_PRODUCT)
        assert chopping_cart.text == name_producr.text, 'куплено не то что нужно'
        assert price_in_cart.text == price_in_product.text, 'стоимость товара и корзины не совпадает'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductLocators.SHOPPING_CART), "Сообщение об успехе отображается, но не должно быть"

    def should_is_disappeared(self):
        assert self.is_disappeared(
            *ProductLocators.SHOPPING_CART), "Сообщение об успехе отображается, но должно пропасть"

    # def solve_quiz_and_get_code(self):
    #     alert = self.browser.switch_to.alert
    #     x = alert.text[4:7]
    #     y = self.calc(x)
    #     alert.send_keys(y)
    #     alert.accept()
    #
    # def calc(self, x):
    #     return str(math.log(abs(12 * math.sin(int(x)))))
