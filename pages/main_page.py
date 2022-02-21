from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()


    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")


#link = "http://selenium1py.pythonanywhere.com/"


#def test_guest_can_go_to_login_page(browser):
#   browser.get(link)
#    go_to_login_page(browser)
