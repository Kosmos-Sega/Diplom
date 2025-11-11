from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

def test_assign_leave(driver, self=None):
    LoginPage(driver).open()
    LoginPage(driver).login("Admin", "admin123")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(.,'Leave')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(.,'Assign Leave')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("Test User")

    from_date_input = self.driver.find_element(By.XPATH, "//input[@placeholder='From']")
    from_date_input.clear()
    from_date_input.send_keys("2025-11-15")

    to_date_input = self.driver.find_element(By.XPATH, "//input[@placeholder='To']")
    to_date_input.clear()
    to_date_input.send_keys("2025-11-20")

    casual_leave_option = self.driver.find_element(By.XPATH, "//span[text()='Casual Leave']")
    casual_leave_option.click()

    assign_button = driver.find_element(By.XPATH, By.XPATH, "//button[contains(text(), 'Assign')]")
    assign_button.click()
    assert "success" in driver.page_source.lower() or "assigned" in driver.page_source.lower()
