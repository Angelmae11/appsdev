import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def webdriver_setup():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    yield driver
    driver.quit()
def test_login(webdriver_setup):
    driver = webdriver_setup
    driver.find_element(By.ID, "username").send_keys("student")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("Password123")
    time.sleep(1)
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    assert "Logged In Successfully" in driver.page_source
def test_negative_username(webdriver_setup):
    driver = webdriver_setup
    driver.find_element(By.ID, "username").send_keys("incorrectUser")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("Password123")
    time.sleep(1)
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    assert "Your username is invalid!" in driver.page_source
def test_negative_password(webdriver_setup):
    driver = webdriver_setup
    driver.find_element(By.ID, "username").send_keys("student")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("incorrectPassword")
    time.sleep(1)
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    assert "Your password is invalid!" in driver.page_source
