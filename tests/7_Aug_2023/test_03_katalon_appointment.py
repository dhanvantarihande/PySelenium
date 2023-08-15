import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Test Cases To Automation  (These are the Manual Steps)
# Steps
# Open This Page "https://katalon-demo-cura.herokuapp.com/"
# Click on the Make Appointment Button
# Then Put Username, Password, and Click Login
# After that in the Select Box --> Select the 2nd Option, Select Check Box, Select Radio Box, Select
# Enter the Date and Text and Click Book Appointment
# In the End We'll Verify that the Appointment Confirmation Message is Visible on the Page


@pytest.mark.negative
def test_katalon_appointment_negative():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    # Click on the Make Appointment Button
    # < a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    # class ="btn btn-dark btn-lg" > Make Appointment
    # < /a >
    link = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # LINK_TEXT means Full Match
    # PARTIAL_LINK_TEXT means We don't know the Exact Match
    link.click()

    # Then Put Username, Password, and Click Login
    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")

    # PASSWORD
    password = driver.find_element(By.NAME, "password")
    password.send_keys("John Doe")

    # # LOGIN BUTTON
    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    assert "Login failed! " in error_message.text


@pytest.mark.positive
def test_katalon_appointment():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    # Click on the Make Appointment Button
    # < a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    # class ="btn btn-dark btn-lg" > Make Appointment
    # < /a >
    link = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # LINK_TEXT means Full Match
    # PARTIAL_LINK_TEXT means We don't know the Exact Match
    link.click()

    # Then Put Username, Password, and Click Login
    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")

    # PASSWORD
    Password = driver.find_element(By.NAME, "password")
    Password.send_keys("ThisIsNotAPassword")

    # # LOGIN BUTTON
    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()

    # After that in the Select Box --> DropDown, Select the 2nd Option, Select Check Box, Select Radio Box, Select
    # DropDown
    dropdown = Select(driver.find_element(By.ID, "combo_facility"))
    dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")

    # SELECT CHECK BOX
    driver.find_element(By.ID, "chk_hospotal_readmission").click()

    # SELECT RADIO BUTTON (2ND OPT)
    driver.find_element(By.NAME, "programs").click()

    # Enter the Date and Text
    driver.find_element(By.ID, "txt_visit_date").send_keys(12 / 12 / 1991)

    # COMMENT AREA
    driver.find_element(By.NAME, "comment").send_keys("I Have a Fever Including Cough")

    # CLICK BOOK APPOINTMENT BUTTON
    driver.find_element(By.ID, "btn-book-appointment").click()

    # VERIFY THE APPOINTMENT CONFIRMATION MESSAGE
    heading_h2 = driver.find_element(By.TAG_NAME, "h2")
    assert "Appointment Confirmation" in heading_h2.text

    time.sleep(10)

    # < select
    # id = "combo_facility"
    # name = "facility"
    # class ="form-control"
    # >

    # USERNAME
    # <input
    # type="text"
    # class="form-control"
    # id="txt-username"
    # name="username"
    # placeholder="Username"
    # value="" autocomplete="off"#
    # >

    # PASSWORD
    # < input
    # type = "password"
    # class ="form-control"
    # id="txt-password"
    # name="password"
    # placeholder="Password"
    # value="" autocomplete="off"
    # >

    # LOGIN BUTTON
    # < button
    # id = "btn-login"
    # type = "submit"
    # class ="btn btn-default"
    # > Login < /button >

    # DROPDOWN
    # < select
    # id = "combo_facility"
    # name = "facility"
    # class ="form-control"
    # >

    # SELECT 2ND OPTION
    # <
    # option
    # value = "Hongkong CURA Healthcare Center" >
    # Hongkong CURA Healthcare Center
    # < / option >

    # SELECT CHECK BOX
    # <label for="chk_hospotal_readmission"
    # class="checkbox-inline">
    # <input type="checkbox"
    # id="chk_hospotal_readmission"
    # name="hospital_readmission"
    # value="Yes"> Apply for hospital readmission
    # </label>

    # SELECT RADIO BUTTON (2ND OPT)
    # <
    # input
    # type = "radio"
    # name = "programs"
    # id = "radio_program_medicaid"
    # value = "Medicaid" >

    # ENTER TIME AND DATE
    # <
    # input
    # type = "text"
    # class ="form-control"
    # id="txt_visit_date"
    # name="visit_date"
    # placeholder="dd/mm/yyyy"
    # autocomplete="off"
    # required=""
    # >

    # COMMENT AREA (TEXT AREA)
    # <
    # textarea
    # class ="form-control"
    # id="txt_comment"
    # name="comment"
    # placeholder="Comment"
    # rows="10" >
    # < /textarea >

    # CLICK BOOK APPOINTMENT BUTTON
    # <
    # button
    # id = "btn-book-appointment"
    # type = "submit"
    # class ="btn btn-default" >
    # Book Appointment < /button >

    # VERIFY THE APPOINTMENT CONFIRMATION MESSAGE
    # < h2 >
    # Appointment Confirmation < / h2 >
