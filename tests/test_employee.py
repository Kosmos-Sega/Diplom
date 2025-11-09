from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time


def test_add_employee(driver):
    LoginPage(driver).open()
    LoginPage(driver).login("Admin", "admin123")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(.,'PIM')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(.,'Add')]").click()
    time.sleep(3)
    driver.find_element(By.NAME, "firstName").send_keys("Test")
    driver.find_element(By.NAME, "lastName").send_keys("User")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    # открылась страница с личными данными сотрудника
    assert "personal" in driver.current_url.lower() or driver.find_element(By.XPATH, "//h6").text != ""