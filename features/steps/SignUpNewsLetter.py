from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


@given(u'chrome browser is launched')
def userOnFullTimeCoursesPage(context):
    context.driver = webdriver.Chrome()


@when(u'open home page')
def openHomePage(context):
    context.driver.get("https://www.np.edu.sg/home")
    context.driver.maximize_window()


@then(u'the user inputs {emailInput} as email and clicks on "Sign up" button')
def inputEmailAndSignUp(context, emailInput):
    emailInputElement = context.driver.find_element(By.XPATH, '//*[@id="subscribeEmail"]')
    emailInputElement.send_keys(emailInput)
    context.driver.execute_script("arguments[0].scrollIntoView();", emailInputElement)
    sleep(3)

    context.driver.find_element(By.XPATH, '//*[@id="button-signup"]').click()
    sleep(8)


@then(u'the user successfully subscribed to the newsletter')
def verifyEmail(context):
    assert context.driver.current_url == "https://www.np.edu.sg/subscription-successful"
    sleep(3)


@then(u'the user inputs {incorrectEmail} and clicks on "Sign up" button')
def inputIncorrectEmailAndSignUp(context, incorrectEmail):
    emailInputElement = context.driver.find_element(By.XPATH, '//*[@id="subscribeEmail"]')
    emailInputElement.send_keys(incorrectEmail)
    context.driver.execute_script("arguments[0].scrollIntoView();", emailInputElement)
    sleep(3)

    context.driver.find_element(By.XPATH, '//*[@id="button-signup"]').click()
    sleep(8)


@then(u'an error message will be displayed')
def verifyErrorMessage(context):
    assert context.driver.find_element(By.XPATH, '//*[@id="pvEmailValidation"]').is_displayed()
    sleep(3)
    