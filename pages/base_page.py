from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://shop.cureskin.com/'
        self.tos_url = 'https://shop.cureskin.com/policies/terms-of-service'
        self.refund_url = 'https://shop.cureskin.com/policies/refund-policy'
        self.privacy_url = 'https://shop.cureskin.com/policies/privacy-policy'
        self.shipping_url = 'https://shop.cureskin.com/policies/shipping-policy'
        self.results_url = 'https://shop.cureskin.com/search?q=cure'

    def open_base_url(self, end_url=''):
        url = f'{self.base_url}{end_url}'
        print(f'Opening URL: {url}')
        self.driver.get(url)

    def open_results_url(self, end_url=''):
        url = f'{self.results_url}{end_url}'
        print(f'Opening Search Results URL: {url}')
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def verify_policy_url(self, policy_url):
        self.wait.until(EC.url_contains(policy_url))
