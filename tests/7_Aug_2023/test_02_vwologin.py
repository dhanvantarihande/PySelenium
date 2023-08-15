# This Below Part will Done By Selenium
import logging

# Open the Browser
# Navigate to a URL
# Find the Email Web Element and put Email Id = "abc@gmail.com"
# Find the Password InputBox and Enter the Password = pass123
# Click on the Signin Button


# Verify that the Dashboard is Loaded - Pytest will Do Verification
# Create a Report to send to QA Lead - HTML --> Allure Report

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_vwologin2():
    # Selenium API - Create Session
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the Browser
    # Navigate to URL
    # Navigate a Particular URL Use this Command -> driver.get  # This will Navigate To the Existing Session
    driver.get("https://app.vwo.com")

    # Find_elements by_link_text: Finds an anchor element (a) by its visible text.
    # Find_elements by_partial_link_text: Finds an anchor element (a) by a partial match of its visible text

    # < a
    # href = "https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class ="text-link"
    # data-qa="bericafeqo" >
    # Start a free trial
    # < /a >

    # ID = 'id'
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SECTOR = "css selector"

    # Which one is Faster
    # ID, NAME, CLASS NAME, LINK TEXT, PARTIAL LINK TEXT, CSS SELECTOR, XPATH
    # CSS SELECTOR  > XPATH --> True/False (Many people say css selector is better than xpath)
    # It Depends Upon Which OS ,Browser We are talking about
    # CSS Selector and XPATH is very small



    # link = driver.find_element(By.LINK_TEXT,"Start a free trial")
    link = driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    link.click()



