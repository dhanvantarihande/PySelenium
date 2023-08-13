# This Below Part will Done By Selenium

# Open the Browser
# Navigate to a URL
# Find the Email Web Element and put Email Id = "abc@gmail.com"
# Find the Password InputBox and Enter the Password = pass123
# Click on the Signin Button


# Verify that the Dashboard is Loaded - Pytest will Do Verification
# Create a Report to send to QA Lead - HTML --> Allure Report

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

def test_vwologin():
    # Selenium API - Create Session
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the Browser
    # Navigate to URL
    # Navigate a Particular URL Use this Command -> driver.get  # This will Navigate To the Existing Session
    driver.get("https://app.vwo.com")

    # Find the Email Web Element and put Email Id = "abc@gmail.com"
    # Find the Password InputBox and Enter the Password = pass123
    # Click on the Signin Button

    # < input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    # Selenium Provides --> How to Find the Elements
    # Find_elements by_id: Finds an element by its unique id attribute.
    # Find_elements by_name: Finds an element by its name attribute.
    # Find_elements by_link_text: Finds an anchor element (a) by its visible text.
    # Find_elements by_partial_link_text: Finds an anchor element (a) by a partial match of
    # Find_elements by_tag_name: Finds an element by its HTML tag name (e.g., "div", "input")
    # Find_elements by_class_name: Finds an element by its CSS class name.

    email_addreess_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.NAME, "password")

    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")

    # Sending the data email and password and Clicking on the button
    # sendKeys and Click()
    email_addreess_ele.send_keys("93npu2yyb0@esiix.com")
    password_ele.send_keys("Wingify@123")

    sign_in_button_ele.click()

    time.sleep(5)


    LOGGER.info('title is' + driver.title)
    # Verify that the Dashboard is Loaded - Pytest will Do Verification
    assert "Dashboard" in driver.title

    driver.refresh()
    driver.get("https://sdet.live")
    driver.back()
    driver.forward()
