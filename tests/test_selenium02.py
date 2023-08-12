import pytest
from selenium import webdriver
import logging


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver



def test_open_url_verify_title(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://app.vwo.com")
    print(driver.title)

    # Intentional Logging to user
    LOGGER.info("This is Information Logs")
    LOGGER.warning("This is Warning Logs")
    LOGGER.error("This is Error Logs")
    LOGGER.critical("This is Critical Logs")
    assert "Login - VWO" == driver.title