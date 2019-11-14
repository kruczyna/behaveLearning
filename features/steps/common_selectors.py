from selenium.webdriver.common.by import By

# MAIN UI
page_body = (By.CSS_SELECTOR, '#page')

# MAIN BUTTONS
contact_us = (By.CSS_SELECTOR, '#contact-link')

# CONTACT US
# page UI elements
subject_heading = (By.CSS_SELECTOR, '#uniform-id_contact')
select_customer_service = (By.CSS_SELECTOR, 'option[value="2"]')
email_address = (By.CSS_SELECTOR, '#email')
order_reference = (By.CSS_SELECTOR, '#id_order')
attach_file = (By.CSS_SELECTOR, '#uniform-fileUpload')
message_textarea = (By.CSS_SELECTOR, '#message')

form_success = (By.CSS_SELECTOR, '.alert.alert-success')
form_error = (By.CSS_SELECTOR, '.alert.alert-danger')
field_error = 'rgba(241, 51, 64, 1)'

# page buttons
send_button = (By.CSS_SELECTOR, '#submitMessage')
