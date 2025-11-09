from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
import time

def test_login_success(driver):
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "admin123")
    time.sleep(2)
    assert "dashboard" in driver.current_url.lower()

def test_login_invalid(driver):
    page = LoginPage(driver)
    page.open()
    page.login("Admin", "wrongpass")
    time.sleep(2)
    err = driver.find_element(By.XPATH,"//p[contains(@class,'oxd-alert-content')]").text
    assert "Invalid" in err or "credentials" in err.lower()
