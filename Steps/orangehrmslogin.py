from selenium.webdriver.support import expected_conditions as EC

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@when('User enters the username "{user}" and password "{pwd}"')
def enterUserDetails(context,user,pwd):
    username_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
    )
    username_field.send_keys(user)

    # Wait until the password input is visible
    password_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
    )
    password_field.send_keys(pwd)



@when('User clicks on login')
def clickLogin(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()



@when('Validate that user able to see the home page')
def verifyHomePage(context):
    try:
        text=context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
    except:
        context.driver.close()
        assert False,"Test Failed"
    assert text == "Dashboard"



