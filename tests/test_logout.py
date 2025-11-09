from pages.login_page import LoginPage
import time
from selenium.webdriver.common.by import By

def test_logout(driver):
    LoginPage(driver).open()
    LoginPage(driver).login("Admin", "admin123")
    time.sleep(2)
    driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Logout')]").click()
    time.sleep(2)
    assert "login" in driver.current_url.lower() or "signin" in driver.current_url.lower()
