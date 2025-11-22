from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC


def test_assign_leave(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)

    leave_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Leave')]")))
    leave_menu.click()

    assign_leave_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Assign Leave')]")))
    assign_leave_link.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Assign Leave']")))

    employee_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type for hints...']")))
    employee_field.send_keys("John")
    time.sleep(2)

    suggestion = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option'][1]")))
    suggestion.click()

    leave_type_dropdown = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[text()='Leave Type']/following::div[1]")))
    leave_type_dropdown.click()

    vacation_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='option']//span[text()='CAN - Vacation']")))
    vacation_option.click()

    date_inputs = driver.find_elements(By.XPATH, "//input[@placeholder='yyyy-dd-mm']")
    date_inputs[0].clear()
    date_inputs[0].send_keys("2025-12-01")
    date_inputs[1].clear()
    date_inputs[1].send_keys("2025-12-03")   # на этом этапе ошибка, эта дата записается плюсом к дате по умолчанию, т.е. clear не работает

    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_btn.click()

    success_msg = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'oxd-toast')]//p[contains(text(), 'Success')]")))

    assert "Success" in success_msg.text