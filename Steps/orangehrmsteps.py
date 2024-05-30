from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'User launch chrome browser')
def launchBrowser(context):
    # context.driver=webdriver.Chrome(executable_path='./Drivers/chromedriver.exe')
    context.driver=webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

@when('User access the url')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

@then('Verify that user should able see the logo')
def verifyLogo(context):
    password_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//img[@alt='company-branding']"))
    )
    status=context.driver.find_element(By.XPATH,"//img[@alt='company-branding']")
    assert status.is_displayed()

@then('Close the browser')
def closeBowser(context):
    context.driver.close()
