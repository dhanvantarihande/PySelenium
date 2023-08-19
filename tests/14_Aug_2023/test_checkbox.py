import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_checkbox_testing():
    # LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    checkbox_one = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")
    checkbox_one.click()
    time.sleep(15)

    # I want to Check the Checkbox which is Not Selected
    for c in checkboxes:
        if not c.is_selected():
            c.click()
