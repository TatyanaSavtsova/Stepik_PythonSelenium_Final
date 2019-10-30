from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def product_should_be_added_to_basket(self):
        self.should_be_success_alert()
        self.should_be_product_name_in_alert()
        self.should_be_price_alert()
        self.should_be_product_price_in_alert()

    #def get_product_name(self):
        #return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text

    #def get_price(self):
        #return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT).text

    def should_be_success_alert(self):
        assert "has been added to your basket." in self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT).text, \
            "There is no success alert"

    def should_be_product_name_in_alert(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text,\
            "Product name in success alert doesn't math the name of added product"

    def should_be_price_alert(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_ALERT), "Price alert is not present"

    def should_be_product_price_in_alert(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, \
            "Product price in price alert doesn't math the price of added product"
