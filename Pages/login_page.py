from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert (self.browser.current_url, *LoginPageLocators.LOGIN_URL, "URL is not valid")

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL), "Email login form is not visible"
        assert self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD), "Password login form is not visible"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL), "Email registration form is not visible"
        assert self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD), "Password registration form is not visible"
        assert self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT), "Password confirmation form is not visible"