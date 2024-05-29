import pytest
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.AddNewCustomerPage import AddNewCustomer
from pageObjects.CustomersPage import Customers
from pageObjects.DashboardPage import Dashboard
from pageObjects.LoginPage import Login


class Test_002_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("************** Test_002_AddCustomer****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.db = Dashboard(self.driver)
        self.db.clickOnCustomersMenu()
        self.db.clickOnCustomersMenuItem()
        self.cu = Customers(self.driver)
        self.cu.clickOnAddNew()
        self.an = AddNewCustomer(self.driver)
        self.an.fillCustomerDetails()
        self.an.clickOnSave()
