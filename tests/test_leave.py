from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

def test_assign_leave(driver):
    LoginPage(driver).open()
    LoginPage(driver).login("Admin", "admin123")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(.,'Leave')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Assign Leave')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("Test User")
    driver.find_element(By.XPATH, "//input[@placeholder='yyyy-mm-dd']").send_keys("2025-12-01") # исправить
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    assert "success" in driver.page_source.lower() or "assigned" in driver.page_source.lower()
