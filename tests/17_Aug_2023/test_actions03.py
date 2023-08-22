import time

import perform as perform
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By


def test_03_actions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    # SCROLLING
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    # ActionChains(driver).scroll_to_element(iframe).perform()
    scroll_origin = ScrollOrigin.from_element(iframe)
    ActionChains(driver).scroll_from_origin(scroll_origin, 0, 200).perform()


    ## DOUBLE CLICK
    # clickable = driver.find_element(By.ID, "clickable")
    # ActionChains(driver) \
    #     .double_click(clickable) \
    #     .perform()

    # hoverable = driver.find_element(By.ID, 'hover')
    # ActionChains(driver)\
    #     .move_to_element(hoverable)\
    #     .perform()

    # DRAGGABLE AND DROPPABLE
    # draggable = driver.find_element(By.ID, "draggable")
    # droppable = driver.find_element(By.ID, "droppable")
    # ActionChains(driver).drag_and_drop(draggable,droppable).perform()


    time.sleep(100)
