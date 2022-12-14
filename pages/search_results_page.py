from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):
    FILTER_LOCATORS = \
        {"Pricefilter": (By.CSS_SELECTOR, "#Details-1-template--14367827656788__main summary div span"),
         "low_value": (By.CSS_SELECTOR, "input#Filter-Price-GTE.field__input"),
         "high_value": (By.CSS_SELECTOR, "input#Filter-Price-LTE.field__input"),
         "Pricefilter2": (By.CSS_SELECTOR,"#Facet-1-template--14367827656788__main.facets__display")}

    def open_search_results_url(self):
        self.open_results_url()

    def click_filter_name(self, filter_name):
        self.find_element(*self.FILTER_LOCATORS[filter_name]).click()
        sleep(2)

    def enter_low_value(self, low_value):
        low_element = self.find_element(*self.FILTER_LOCATORS["low_value"])
        low_element.clear()
        low_element.send_keys(low_value)
        sleep(2)

    def enter_high_value(self, high_value):
        high_element = self.find_element(*self.FILTER_LOCATORS["high_value"])
        high_element.clear()
        high_element.send_keys(high_value)
        sleep(2)

    def close_filter(self, filter_name):
        filter_name += '2'
        print(filter_name)
        self.find_element(*self.FILTER_LOCATORS[filter_name]).click()
        sleep(2)