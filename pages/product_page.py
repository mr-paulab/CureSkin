from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    PRODUCT_LINKS = \
        {"CureSkin Under Eye Gel": 'https://shop.cureskin.com/products/cureskin-under-eye-gel',
         "CureSkin Cleansing Gel": 'https://shop.cureskin.com/products/cureskin-cleansing-gel'}

    FPRODUCT_ATC_BTN = (By.CSS_SELECTOR, ".product-form__submit.button")
    BUY_NOW_BTN = (By.CSS_SELECTOR, ".shopify-payment-button__button.shopify-payment-button__button--unbranded")
    CART_LINK = (By.CSS_SELECTOR, "[href='https://shop.cureskin.com/cart'")
    FIRST_ITEM = (By.ID, "CartItem-1")
    SECOND_ITEM = (By.ID, "CartItem-2")
    BUYITNOW_URL = "//shop.cureskin.com/checkouts/"

    def open_first_product_page(self):
        self.open_fproduct_url()

    def add_to_cart_button(self):
        self.find_element(*self.FPRODUCT_ATC_BTN).click()

    def open_second_product_page(self):
        self.open_sproduct_url()

    def buy_now_button(self):
        self.find_element(*self.BUY_NOW_BTN).click()

    def click_cart_link(self):
        self.find_element(*self.CART_LINK).click()

    def see_first_cart_item(self):
        assert (self.find_element(*self.FIRST_ITEM)), '1st cart item not found'

    def see_second_cart_item(self):
        assert (self.find_element(*self.SECOND_ITEM)), '2nd cart item not found'

    def verify_buyitnow(self, value):
        self.verify_buyitnow_url(self.BUYITNOW_URL)
