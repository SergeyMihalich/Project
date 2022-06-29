import time

from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_reg = self.browser.find_element(*BasePageLocators.EMAIL)
        email_reg.send_keys(email)
        pass_reg = self.browser.find_element(*BasePageLocators.PASSWORD_1)
        pass_reg.send_keys(password)
        pass_reg = self.browser.find_element(*BasePageLocators.PASSWORD_2)
        pass_reg.send_keys(password)
        button_reg = self.browser.find_element(*BasePageLocators.REG_BUTTON)
        button_reg.click()


    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'url не совпадает'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'отсутствует поле для логина'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'отсутствует поле регистрации'

