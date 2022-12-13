from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep


@given('open main shopping page')
def open_main_shopping(context):
    context.driver.get("https://shop.cureskin.com/")
    print(f'Opening https://shop.cureskin.com/')


@when('click on {value}')
def click_on_link(context, value):
    context.app.main_page.click_on_link(value)


@then('verify page by {value}')
def verify_page_url(context, value):
    context.app.main_page.verify_url(value)
