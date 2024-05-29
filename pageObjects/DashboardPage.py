from selenium.webdriver.common.by import By


class Dashboard:
    link_customers_xpath="//i[@class='nav-icon far fa-user']/..//p"
    link_customersopt_xpath="//li[@class='nav-item has-treeview menu-is-opening menu-open']//i[@class='nav-icon far fa-dot-circle']/../p[contains(text(),'Customers')]"

    def __init__(self,driver):
        self.driver=driver
    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.link_customers_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.link_customersopt_xpath).click()
