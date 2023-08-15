# Selenium Provides --> How to Find the Elements
# Find_elements by_id: Finds an element by its unique id attribute.
# Find_elements by_name: Finds an element by its name attribute.
# Find_elements by_link_text: Finds an anchor element (a) by its visible text.
# Find_elements by_partial_link_text: Finds an anchor element (a) by a partial match of
# Find_elements by_tag_name: Finds an element by its HTML tag name (e.g., "div", "input")
# Find_elements by_class_name: Finds an element by its CSS class name.


# import logging
# import password

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select


# Test Cases To Automation  (These are the Manual Steps)
# Steps
# Open This Page "https://katalon-demo-cura.herokuapp.com/"
# Click on the Make Appointment Button
# Then Put Username, Password, and Click Login
# After that in the Select Box --> Select the 2nd Option, Select Check Box, Select Radio Box, Select
# Enter the Date and Text and Click Book Appointment
# In the End We'll Verify that the Appointment Confirmation Message is Visible on the Page

# def test_katalon_appointment():
#     LOGGER = logging.getLogger(__name__)
#     driver = webdriver.Chrome()
#     driver.get("https://katalon-demo-cura.herokuapp.com/")
#     driver.maximize_window()

# Click on the Make Appointment Button
# < a
# id = "btn-make-appointment"
# href = "./profile.php#login"
# class ="btn btn-dark btn-lg" > Make Appointment
# < /a >
# link = driver.find_element(By.LINK_TEXT, "Make Appointment")
# LINK_TEXT means Full Match
# PARTIAL_LINK_TEXT means We don't know the Exact Match
# link.click()

# Then Put Username, Password, and Click Login
# username = driver.find_element(By.ID, "txt-username")
# username.send_keys("John Doe")

# PASSWORD
# Password = driver.find_element(By.NAME, "password")
# Password.send_keys("ThisIsNotAPassword")

# # LOGIN BUTTON
# login_button = driver.find_element(By.ID, "btn-login")
# login_button.click()

# After that in the Select Box --> DropDown, Select the 2nd Option, Select Check Box, Select Radio Box, Select
# DropDown
# dropdown = Select(driver.find_element(By.ID, "combo_facility"))
# dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")

# time.sleep(5)

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


#  2ND ATTEMPT SUCCESSFUL

# import logging

# Test Cases To Automation  (These are the Manual Steps)
# Steps
# Open This Page "https://katalon-demo-cura.herokuapp.com/"
# Click on the Make Appointment Button
# Then Put Username, Password, and Click Login
# After that in the Select Box --> Select the 2nd Option, Select Check Box, Select Radio Box, Select
# Enter the Date and Text and Click Book Appointment
# In the End We'll Verify that the Appointment Confirmation Message is Visible on the Page

# def test_katalon_appointment():
#     LOGGER = logging.getLogger(__name__)
#     driver = webdriver.Chrome()
#     driver.get("https://katalon-demo-cura.herokuapp.com/")
#     driver.maximize_window()

# Click on the Make Appointment Button
# < a
# id = "btn-make-appointment"
# href = "./profile.php#login"
# class ="btn btn-dark btn-lg" > Make Appointment
# < /a >
# link = driver.find_element(By.LINK_TEXT, "Make Appointment")
# LINK_TEXT means Full Match
# PARTIAL_LINK_TEXT means We don't know the Exact Match
# link.click()

# username = driver.find_element(By.ID, "txt-username")
# username.send_keys("John Doe")

# Password = driver.find_element(By.NAME, "password")
# Password.send_keys("ThisIsNotAPassword")

# login_button = driver.find_element(By.ID, "btn-login")
# login_button.click()

# dropdown = Select(driver.find_element(By.ID, "combo_facility"))
# dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")import logging
# import password
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select


# Test Cases To Automation  (These are the Manual Steps)
# Steps
# Open This Page "https://katalon-demo-cura.herokuapp.com/"
# Click on the Make Appointment Button
# Then Put Username, Password, and Click Login
# After that in the Select Box --> Select the 2nd Option, Select Check Box, Select Radio Box, Select
# Enter the Date and Text and Click Book Appointment
# In the End We'll Verify that the Appointment Confirmation Message is Visible on the Page

# def test_katalon_appointment():
#     LOGGER = logging.getLogger(__name__)
#     driver = webdriver.Chrome()
#     driver.get("https://katalon-demo-cura.herokuapp.com/")
#     driver.maximize_window()

# Click on the Make Appointment Button
# < a
# id = "btn-make-appointment"
# href = "./profile.php#login"
# class ="btn btn-dark btn-lg" > Make Appointment
# < /a >
# link = driver.find_element(By.LINK_TEXT, "Make Appointment")
# LINK_TEXT means Full Match
# PARTIAL_LINK_TEXT means We don't know the Exact Match
# link.click()


# username = driver.find_element(By.ID, "txt-username")
# username.send_keys("John Doe")


# Password = driver.find_element(By.NAME, "password")
# Password.send_keys("ThisIsNotAPassword")

# login_button = driver.find_element(By.ID, "btn-login")
# login_button.click()

# dropdown = Select(driver.find_element(By.ID, "combo_facility"))
# dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")
