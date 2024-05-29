from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class Login:
    textbox_username_xpath = "//input[@type='email']"
    textbox_password_xpath = "//input[@type='password']"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_xpath = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        try:
            username_input = self.driver.find_element(By.XPATH, self.textbox_username_xpath)
            username_input.clear()
            username_input.send_keys(username)
        except NoSuchElementException:
            print("Username textbox not found")

    def setPassword(self, password):
        try:
            password_input = self.driver.find_element(By.XPATH, self.textbox_password_xpath)
            password_input.clear()
            password_input.send_keys(password)
        except NoSuchElementException:
            print("Password textbox not found")

    def clickLogin(self):
        try:
            login_button = self.driver.find_element(By.XPATH, self.button_login_xpath)
            login_button.click()
        except NoSuchElementException:
            print("Login button not found")

    def clickLogout(self):
        try:
            logout_link = self.driver.find_element(By.XPATH, self.link_logout_xpath)
            logout_link.click()
        except NoSuchElementException:
            print("Logout link not found")
