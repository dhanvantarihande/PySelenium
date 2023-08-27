import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


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
    js_ex = driver.execute_script
    element = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    element.click()
    time.sleep(2)
    js_ex("arguments[0].click()", element)

    # title = js_ex("return document.title")
    # print(title)

    # js_ex("windows.scrollBy(0,100)")

    btn_add = driver.find_elements(By.CLASS_NAME, "added-manually")
    print(len(btn_add))
    time.sleep(5)

    # driver.get("https://thetestingacademy.com/")
    # js_ex("window.scrollBy(0,600)")
    # time.sleep(5)
