import os
import pytest
from pageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test001Login:
    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.usefixtures("setup")
    def test_homepage_title(self,setup):
        self.logger.info("************** Test Home Page Title ****************")
        self.logger.info("************** Verifying Home Page Title ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("************** Home Page Title test is passed **********")
            assert True
        else:
            screenshot_path = os.path.join(os.getcwd(), "Screenshots", "login_failed.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("************* Home Page Title test is failed ***********")
            # self.driver.save_screenshot(".\\Screenshots")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.usefixtures("setup")
    def test_login(self,setup):
        self.logger.info("************** Test Login Title ***********************")
        self.logger.info("************** Verify Login Title *********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("************** Test Login Title is passed ************")
            assert True
        else:
            screenshot_path = os.path.join(os.getcwd(), "Screenshots", "login_failed.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("************** Test Login Title is failed ************")
            assert False
        self.driver.close()
