from selenium.webdriver.common.by import By


class Customers:
    textboxlist_customersearch_xpath="//div[@class='search-body ']//input"
    link_addnew_xpath="//div[@class='float-right']//a"

    def __init__(self,driver):
        self.driver=driver

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.link_addnew_xpath).click()