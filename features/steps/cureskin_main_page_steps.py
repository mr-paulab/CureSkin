from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


TANDC_POLICY = (By.CSS_SELECTOR, "[href*='/policies/terms-of-service']")
REFUND_POLICY = (By.CSS_SELECTOR, "[href*='/policies/refund-policy']")
PRIVACY_POLICY = (By.CSS_SELECTOR, "[href*='/policies/privacy-policy']")
SHIPPING_POLICY = (By.CSS_SELECTOR, "[href*='/policies/shipping-policy']")


@given('open cureskin main shopping page')
def open_cureskin_home(context):
    context.driver.get("https://shop.cureskin.com/")


@when('click on Terms and Conditions link')
def click_tandc_policy(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(TANDC_POLICY), message='T and Cs link not clickable')
    e.click()


@when('click on Refund Policy link')
def click_refund_policy(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(REFUND_POLICY), message='Refund Policy not clickable')
    e.click()


@when('click on Privacy Policy link')
def click_privacy_policy(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(PRIVACY_POLICY), message='Privacy Policy not clickable')
    e.click()


@when('click on Shipping Policy link')
def click_shipping_policy(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SHIPPING_POLICY), message='Shipping Policy not clickable')
    e.click()


@then('verify Terms and Conditions page displays')
def verify_tandc_page(context):
    context.driver.wait.until(EC.title_contains("Terms of service – CureSkin"))
    print(f'Terms and Conditions loaded')


@then('verify Refund Policy page displays')
def verify_tandc_page(context):
    context.driver.wait.until(EC.title_contains("Refund policy – CureSkin"))
    print(f'Refund Policy loaded')


@then('verify Privacy Policy page displays')
def verify_tandc_page(context):
    context.driver.wait.until(EC.title_contains("Privacy policy – CureSkin"))
    print(f'Privacy Policy loaded')


@then('verify Shipping Policy page displays')
def verify_tandc_page(context):
    context.driver.wait.until(EC.title_contains("Shipping policy – CureSkin"))
    print(f'Shipping Policy loaded')
