import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_add_button_then_enter_text(driver):
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    time.sleep(10)

    driver.find_element(By.ID, "add_btn").click()
    time.sleep(10)

    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "row2_input"))
    )
    time.sleep(10)

    input_field.send_keys("Selenium Test")
    time.sleep(10)

    driver.find_element(By.ID, "save_btn").click()
    time.sleep(10)

    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "confirmation"))
    )
    time.sleep(10)

    assert success.text == "Row 2 was saved"


def test_click_enable_button(driver):
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    time.sleep(10)

    driver.find_element(By.ID, "enable_btn").click()
    time.sleep(10)

    input_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "input_field"))
    )
    time.sleep(10)

    input_field.send_keys("Enabled!")
    time.sleep(10)

    assert input_field.get_attribute("value") == "Enabled!"


def test_timeout_exception(driver):
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    time.sleep(10)

    driver.find_element(By.ID, "add_btn").click()
    time.sleep(10)

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "row2_input"))
        )
        assert False, "TimeoutException was expected but did not occur."
    except TimeoutException:
        assert True
