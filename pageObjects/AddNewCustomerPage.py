from selenium.webdriver.common.by import By
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select


class AddNewCustomer:
    textboxlist_customerinfo_xpath="//div[@class='card card-secondary card-outline']//input"
    select_venderid_xpath="//select[@name='VendorId']"
    button_save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    email = random_generator() + "@gmail.com"
    value = random_generator()

    def fillCustomerDetails(self):
        details=self.driver.find_elements(By.XPATH, self.textboxlist_customerinfo_xpath)
        for i in details:
            print(i.get_attribute('type'),i.get_attribute('name'),i.get_attribute('value'))
            if i.get_attribute('name')=='Email':
                i.send_keys(self.email)
            elif i.get_attribute('name')=='Password':
                i.send_keys(self.value)
            elif i.get_attribute('name')=='FirstName':
                i.send_keys(self.value)
            elif i.get_attribute('name')=='LastName':
                i.send_keys(self.value)
            elif i.get_attribute('name')=='Gender':
                if i.get_attribute('value')=='M':
                    i.click()
            elif i.get_attribute('name')=='DateOfBirth':
                i.send_keys("01-11-1995")
            elif i.get_attribute('name') == 'Company':
                i.send_keys(self.value)
            elif i.get_attribute('type') == 'search':
                i.send_keys(self.value)
    def vendorDropdown(self):
        dropdown_element = self.driver.find_element(By.XPATH, self.select_venderid_xpath)
        dropdown = Select(dropdown_element)
        self.dropdown.select_by_index(1)
    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.button_save_xpath).click()




