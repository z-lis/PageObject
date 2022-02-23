from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url(browser=self.browser)
        self.should_be_login_form()
        self.should_be_register_form()

    @staticmethod
    def should_be_login_url(browser):
        assert "login" in browser.current_url, "'login' is not presented in current url"
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
        assert True
