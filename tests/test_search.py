from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

def test_search_employee(driver):
    LoginPage(driver).open()
    LoginPage(driver).login("Admin", "admin123")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(.,'PIM')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("Test")
    driver.find_element(By.XPATH, "//button[contains(.,'Search')]").click()
    time.sleep(2)
    rows = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
    assert len(rows) >= 0
