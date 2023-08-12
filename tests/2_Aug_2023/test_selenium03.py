import pytest
from selenium import webdriver
import logging



# There is Chrome Known as a Function
# Chrome gives the more Functionality
# If we want to Start a Chrome with the Extention with a Particular Window Size,or want to Start with a Proxy
# or want to Start a Chrome with a JavaScripts  Disabled.

def test_login():
    chrome_options = webdriver.ChromeOptions()

    # extension_path = "\Users\Snehal\Downloads\extension\extension_5_9_0_0.crx"
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless=new")
    # chrome_options.add_extension(extension_path)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com")
