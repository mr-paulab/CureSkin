from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    LINK_LOCATORS = \
        {"Terms of Service": (By.CSS_SELECTOR, "[href*='/policies/terms-of-service']"),
         "Refund Policy": (By.CSS_SELECTOR, "[href*='/policies/refund-policy']"),
         "Privacy Policy": (By.CSS_SELECTOR, "[href*='/policies/privacy-policy']"),
         "Shipping Policy": (By.CSS_SELECTOR, "[href*='/policies/shipping-policy']")}

    POLICY_URLS = \
        {"Terms of Service": "//shop.cureskin.com/policies/terms-of-service",
         "Refund Policy": "//shop.cureskin.com/policies/refund-policy",
         "Privacy Policy": "//shop.cureskin.com/policies/privacy-policy",
         "Shipping Policy": "//shop.cureskin.com/policies/shipping-policy"}

    def open_main(self):
        self.open_base_url()

    def click_on_link(self, value):
        self.find_element(*self.LINK_LOCATORS[value]).click()

    def verify_url(self, value):
        self.verify_policy_url(self.POLICY_URLS[value])
