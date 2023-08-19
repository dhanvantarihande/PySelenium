import logging

from selenium import webdriver
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_vwologin():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://app.vwo.com/#/login")

    username = driver.find_element(By.NAME, "username")
    username.send_keys("dhanvantari.hande@gmail.com")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("Reyy0911")

    submit_button = driver.find_element(By.CSS_SELECTOR, "#js-login-btn")
    submit_button.click()

    # .page-heading
    # WebDriverWait(driver, 15).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-heading"))
    # )

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    element = EC.presence_of_element_located((By.CSS_SELECTOR, ".page-heading"))

    
    driver.quit()
