from behave import given, then, step
from selenium.webdriver.support import color

import features.steps.common_selectors as selectors
from steps.common_actions import short_wait


@given('I land on home screen')
def main_page(context):
	context.driver.get('http://automationpractice.com/index.php')


@given('I click Contact Us button')
def contact_us_click(context):
	contact_us = context.driver.find_element(*selectors.contact_us)
	contact_us.click()


@then('I am on CONTACT US page')
def contact_us_click(context):
	short_wait(context.driver, selectors.subject_heading)
	short_wait(context.driver, selectors.order_reference)
	short_wait(context.driver, selectors.email_address)
	short_wait(context.driver, selectors.attach_file)


@given('I click Send button')
def send_button_click(context):
	send_button = context.driver.find_element(*selectors.send_button)
	send_button.click()


@then('I see Invalid email address error')
def invalid_form_message(context):
	short_wait(context.driver, selectors.form_error)


@given('I input "{input_string}" in email field')
def text_input(context, input_string):
	email_field = context.driver.find_element(*selectors.email_address)
	email_field.click()
	email_field.clear()
	email_field.send_keys(input_string)


@step('I click on Contact Us body')
def contact_us_body_click(context):
	contact_us_body = context.driver.find_element(*selectors.page_body)
	contact_us_body.click()


@then('I see email input error')
def email_input_error(context):
	email_field = context.driver.find_element(*selectors.email_address)
	field_error = selectors.field_error
	email_field_color = email_field.value_of_css_property('color')
	print(field_error)
	print(email_field_color)
	assert field_error is email_field_color
