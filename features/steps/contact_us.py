from behave import given, then, when
import features.steps.common_selectors as selectors
# from selenium.webdriver.common.action_chains import ActionChains


@given('I land on home screen')
def main_page(context):
	context.browser.get('http://automationpractice.com/index.php')


@given('I click Contact Us button')
def contact_us_click(context):
	context.driver.find_element(*selectors.contact_us)
