from behave import given, then, step, when
import features.steps.common_selectors as selectors
from features.steps.common_actions import medium_wait


@given('I click main Sign In button')
def click_sign_in(context):
    sign_in_button = context.driver.find_element(*selectors.sign_in)
    sign_in_button.click()


@step('I am on SIGN IN page')
def sign_in_page(context):
    medium_wait(context.driver, selectors.submit_login)
    medium_wait(context.driver, selectors.create_account)


@given('I input "{input_string}" in password field')
def text_input(context, input_string):
    password_field = context.driver.find_element(*selectors.password_field)
    password_field.click()
    password_field.clear()
    password_field.send_keys(input_string)


@when('I click Sign In button')
def click_submit_login(context):
    submit_login = context.driver.find_element(*selectors.submit_login)
    submit_login.click()


@step('I am a logged in user')
def successful_login(context):
    # check for user main buttons
    context.driver.find_element(*selectors.wishlist_button)
    context.driver.find_element(*selectors.addresses_button)
    context.driver.find_element(*selectors.credit_slips_button)
    context.driver.find_element(*selectors.personal_info_button)
    context.driver.find_element(*selectors.orders_button)

    # check user button
    context.driver.find_element(*selectors.user_info)


@given('I click Sign Out button')
def click_sign_out(context):
    sign_out_button = context.driver.find_element(*selectors.sign_out_button)
    sign_out_button.click()
