from behave import given, when, then


@given('open search results page')
def open_search_results(context):
    context.app.search_results_page.open_search_results_url()


@when('click {filter_name} open')
def click_filter_open(context, filter_name):
    context.app.search_results_page.click_filter_name(filter_name)


@then('enter low value {low_value}')
def enter_low_price(context, low_value):
    context.app.search_results_page.enter_low_value(low_value)


@then('enter high value {high_value}')
def enter_high_price(context, high_value):
    context.app.search_results_page.enter_high_value(high_value)


@then('click {filter_name} to close price filter')
def click_filter_close(context, filter_name):
    context.app.search_results_page.close_filter(filter_name)
