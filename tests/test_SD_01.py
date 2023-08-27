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
    URL = "https://selectorshub.com/xpath-practice-page/"
    driver.get(URL)
    element = driver.find_element(By.NAME, "email")
    element.send_keys("dhanvantari123@gmail.com")

    password = driver.find_element(By.ID, "pass")
    password.send_keys("Reyy999")

    com = driver.find_element(By.NAME, "company")
    com.send_keys("TCS")

    mob = driver.find_element(By.NAME, "mobile number")
    mob.send_keys("8352215298")

    sub_btn = driver.find_element(By.XPATH, "//input[@value='Submit']")
    sub_btn.click()

    time.sleep(15)
