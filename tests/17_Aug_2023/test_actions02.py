import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_02_action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # Normal CLICK
    # clickable = driver.find_element(By.ID, "click")
    # ActionChains(driver) \
    #     .click(clickable) \
    #     .perform()

    ## CLICK AND HOLD
    clickable = driver.find_element(By.ID, "click")
    ActionChains(driver) \
        .click_and_hold(clickable) \
        .perform()

    time.sleep(20)



# clickable = driver.find_element(By.ID, "clickable")
#     actions = ActionChains(driver)
#     actions.click_and_hold(clickable).key_down(Keys.SHIFT).send_keys("reyansh").key_up(Keys.SHIFT).perform()