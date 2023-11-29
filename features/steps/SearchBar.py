from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given(u'Chrome brower is Launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome()


@when(u'Open NP page')
def openNPPage(context):
    context.driver.get("https://www.np.edu.sg/home")


@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()


@then(u'Input Search "{item}"')
def searchIT(context, item):
    context.driver.find_element(By.XPATH, '//*[@id="navbarNavDropdown"]/ul/li[8]/button').click()
    sleep(2)
    context.driver.find_element("id", "fsearch").send_keys(item)
    sleep(2)
    context.driver.find_element("id", "fsearch").send_keys(Keys.ENTER)
    sleep(2)

@then(u'Search for Enrolment Criteria')
def searchEnrolement(context):
    context.driver.find_element(By.XPATH, '//*[@id="navbarNavDropdown"]/ul/li[8]/button').click()
    sleep(2)
    context.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[2]/button').click()
    sleep(2)
    context.driver.switch_to.window(context.driver.window_handles[1])
    context.driver.find_element(By.XPATH, '//*[@id="sitesearch-result"]/div[2]/a[1]').click()
    sleep(5)