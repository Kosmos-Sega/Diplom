from selenium.webdriver.common.by import By
import time

class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/web"
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(3)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.BUTTON).click()
