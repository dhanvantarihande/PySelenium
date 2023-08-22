import time

import perform as perform
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By


def test_03_actions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = "https://www.makemytrip.com/"
    driver.get(url)

    time.sleep(30)

    fromCity = driver.find_element(By.ID, "fromCity")
    # fromCity.send_keys("New Delhi")
    actions = ActionChains(driver)
    actions.move_to_element(fromCity).click().send_keys("New Delhi").perform()
