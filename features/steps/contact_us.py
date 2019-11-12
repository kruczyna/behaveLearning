from behave import given, then, when
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
