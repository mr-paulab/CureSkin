from behave import given, when, then
from time import sleep


@given('open url for first product')
def open_product_page(context):
    context.app.product_page.open_first_product_page()


@when('click add to cart button')
def click_add_to_cart(context):
    context.app.product_page.add_to_cart_button()
    sleep(4)


@when('open url for second product')
def open_product_page(context):
    context.app.product_page.open_second_product_page()

@when('click buy it now button')
def click_buy_it_now(context):
    context.app.product_page.buy_now_button()
    sleep(4)

@when('click cart breadcrumb')
def click_cart_breadcrumb_link(context):
    context.app.product_page.click_cart_link()
    sleep(4)

@when('look for first item in cart')
def see_first_item_in_cart(context):
    context.app.product_page.see_first_cart_item()

@then('look for second item in cart')
def see_second_item_in_cart(context):
    context.app.product_page.see_second_cart_item()
