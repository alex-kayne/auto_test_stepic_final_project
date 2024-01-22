from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), 'Basket is not empty'

    def basket_has_zero_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket has items'
