from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    SEARCH_RESULTS = (By.CSS_SELECTOR, "h1 #cart__empty-text")
    expected_text = 'Your cart is empty'

    def verify_element_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        print(actual_text, expected_text)
        assert expected_text in actual_text, \
            f'Expected text {expected_text} is not in {actual_text}'
