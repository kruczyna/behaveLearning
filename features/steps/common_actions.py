from behave_webdriver import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from typing import Tuple
import features.steps.storage as storage


def medium_wait(web_driver: driver, selector: Tuple) -> None:
    """
    Wait for an element to appear in browser. Time value configurable in storage.py
    """
    element_medium_wait = expected_conditions.visibility_of_element_located(selector)
    browser_wait = WebDriverWait(web_driver, storage.medium_timeout)
    browser_wait.until(element_medium_wait)
