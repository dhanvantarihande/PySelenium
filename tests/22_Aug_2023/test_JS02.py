import time

import driver as driver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.utils.JSUtils import JSUtils


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    driver.get(URL)
    js_utils = JSUtils(driver)
    # js_utils.make_alert("Hello")
    # time.sleep(5)

    element = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    js_utils.click_element_by_js(element)
    time.sleep(5)
