from selenium.webdriver.common.by import By

# main buttons
contact_us = (By.CSS_SELECTOR, '#contact-link')

# CONTACT US
# page UI elements
subject_heading = (By.CSS_SELECTOR, '#uniform-id_contact')
email_address = (By.CSS_SELECTOR, '#email')
order_reference = (By.CSS_SELECTOR, '#id_order')
attach_file = (By.CSS_SELECTOR, '#uniform-fileUpload')

form_error = (By.CSS_SELECTOR, '.alert.alert-danger')

# page buttons
send_button = (By.CSS_SELECTOR, '#submitMessage')
