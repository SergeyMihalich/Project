from .base_page import BasePage
from .locators import OpenBasket


class BasketPage(BasePage):
    def should_be_product_in_basket(self):
        assert self.is_not_element_present(*OpenBasket.PRODUCT_IN_BASKET), 'в корзину чтото накидали'

    def should_be_massage_in_basket(self):
        assert self.is_element_present(*OpenBasket.MESSAGE_IN_BASKET), 'в корзине нет сообщения о ее пустоте'
