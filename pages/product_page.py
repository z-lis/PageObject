from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def product_name_must_match(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        successfull_alert = self.browser.find_element(*ProductPageLocators.SUCCESSFUL_ALERT).text
        assert product_name == successfull_alert, "Names of the added product and the product in the basket do not match"

    def product_price_must_match(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert product_price == basket_price, "Prices do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFUL_ALERT), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFUL_ALERT), "Success massage is not disappeared"