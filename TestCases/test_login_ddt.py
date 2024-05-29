import os
import pytest
from pageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils


class Test002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/testData.xlsx"
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.usefixtures("setup")
    def test_login_ddt(self,setup):
        self.logger.info("************** Test_002_DDT_Login *********************")
        self.logger.info("************** Test Login Title ***********************")
        self.logger.info("************** Verify Login DDT Title *********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]
        for r in range(2,self.rows+1):
            self.userName=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.expected = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.userName)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.expected=="Pass":
                    self.logger.info("****Passed****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.expected=="Fail":
                    self.logger.info("****Failed****")
                    self.lp.clickLogout()
            elif act_title!=exp_title:
                if self.expected=="Pass":
                    self.logger.info("*******failed******")
                    lst_status.append("Fail")
                elif self.expected=="Fail":
                    self.logger.info("*********Passed*******")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("******** Login DDT test passed *******")
            self.driver.close()
            assert True
        else:
            self.logger.info("******** Login DDT test failed *******")
            self.driver.close()
            assert False
        self.logger.info("************ End of Login DDT Test **************")
        self.logger.info("**************** Completed TC_LoginDDT_002 ***********")


