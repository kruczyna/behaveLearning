from behave import given, then, step

import features.steps.common_selectors as selectors
from steps.common_actions import medium_wait


@step('I land on home screen')
def main_page(context):
	context.driver.get('http://automationpractice.com/index.php')


@given('I click Contact Us button')
def contact_us_click(context):
	contact_us = context.driver.find_element(*selectors.contact_us)
	contact_us.click()


@then('I am on CONTACT US page')
def contact_us_click(context):
	medium_wait(context.driver, selectors.subject_heading)
	medium_wait(context.driver, selectors.order_reference)
	medium_wait(context.driver, selectors.email_address)
	medium_wait(context.driver, selectors.attach_file)


@step('I click Send button')
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
	css_value = context.driver.find_element(*selectors.email_address).value_of_css_property("color")

	assert css_value == field_error


@then('I see form error')
def empty_message_error(context):
	context.driver.find_element(*selectors.form_error)


@step('I input "{field_input}" in message field')
def input_message_field(context, field_input):
	message_field = context.driver.find_element(*selectors.message_textarea)
	message_field.click()
	message_field.send_keys(field_input)


@step('I select message subject')
def select_subject(context):
	select_field = context.driver.find_element(*selectors.subject_heading)
	select_field.click()
	select_customer_service = context.driver.find_element(*selectors.select_customer_service)
	select_customer_service.click()


@then('I see form success')
def form_success(context):
	medium_wait(context.driver, selectors.form_success)
