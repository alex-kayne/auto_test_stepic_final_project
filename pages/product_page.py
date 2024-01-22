import math

from selenium.common.exceptions import NoAlertPresentException  # в начале файла

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_name_from_current_page(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price_from_current_page(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()
        self.solve_quiz_and_get_code()
        product_name = self.get_product_name_from_current_page()
        product_price = self.get_product_price_from_current_page()
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_ALERT_PRODUCT_NAME) and product_name == self.browser.find_element(
            *ProductPageLocators.SUCCESS_ALERT_PRODUCT_NAME).text, \
            'Product has not been added to basket'
        assert self.is_element_present(
            *ProductPageLocators.INFO_ALERT_PRODUCT_PRICE) and product_price == self.browser.find_element(
            *ProductPageLocators.INFO_ALERT_PRODUCT_PRICE).text, \
            'Basket has wrong total'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT_PRODUCT_NAME), \
            "Success message should disappear, but does not"
