import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_idrive():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.implicitly_wait(20)  # Tell webdriver to wait for 20 sec to Load All the Elements

    # Tell webdriver to wait for 20 sec to Load All the Elements
    # What if ele1, ele2, ele3 they loaded less than 20 sec - then it's a waste of time

    driver.get("https://www.idrive360.com/enterprise/login/")
    # ENTER EMAIL
    username = driver.find_element(By.NAME, "username")
    username.send_keys("dhanvantari.hande911@gmail.com")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("@Reyy0911")
    submit_button = driver.find_element(By.ID, "frm-btn")
    submit_button.click()

    add_button = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id='add-device-header-btn']"))
    )
    add_button.click()

    download_btn = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='id-card-bdy-backup-agent-win']/button"))
    )
    download_btn.click()

    # add_button = WebDriverWait(driver, 15).until(
    #     EC.visibility_of_element_located(By.ID, "add-device-header-btn")
    # )

    time.sleep(100)  # Tell the python interpreter to Wait or Halt the Program for the 100 sec

    # add_button = WebDriverWait(driver, 15).until(
    #     EC.visibility_of_element_located(By.XPATH, "//span[normalize-space()='Add Devices']")

    # add_button = driver.find_element(By.XPATH, "//*[@id='add-device-header-btn']/span")
    # add_button.click()

    # download_btn = driver.find_element(By.XPATH, "//*[@id='id-card-bdy-backup-agent-win']/button")
    # download_btn.click()

    # ENTER EMAIL
    # <
    # input_ngcontent - xdh - c4 = ""
    # autofocus = ""
    # class ="id-form-ctrl ng-pristine ng-valid ng-touched"
    # id="username"
    # name="username"
    # type="email"
    # >

    # ENTER PASSWORD
    # <
    # input_ngcontent - xdh - c4 = ""
    # class ="id-form-ctrl ng-pristine ng-valid ng-to\
    # uched"
    # id="password"
    # name="password"
    # tabindex="0"
    # type="password"
    # >

    # ENTER SIGN IN BUTTON
    # < button_ngcontent - xdh - c4 = ""
    # class ="id-btn id-info-btn-frm"
    # id="frm-btn"
    # type="submit" > Sign in < /button >

    # CLICK ON ADD DEVICE BUTTON
    # < a_ngcontent - eoe - c3 = ""
    # class ="id-btn id-primary-btn-bd id-add-computer id-icons id-tkn-btn"
    # href="javascript:;"
    # id="add-device-header-btn"
    # onclick="openSidebar('id-add-device')" >
    # < svg _ngcontent-eoe-c3="" class ="svg-ico" >
    # < use _ngcontent-eoe-c3=""
    # xlink:href = "../assets/images/svgicons/id-icons.svg#ico-add" > <
    # / use > < / svg > < span
    # _ngcontent - eoe - c3 = "" > Add
    # Devices < / span > < / a >

    # CLICK ON DOWNLOAD BUTTON
    # <
    # button_ngcontent - eoe - c4 = ""
    # class ="id-btn id-info-btn-frm id-tkn-btn id-window-btn"
    # >
    # Download Backup Agent < /button >
