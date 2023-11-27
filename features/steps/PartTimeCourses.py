from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given(u'Chrome browser is Launched')
def launchChromeBrowser(context):
    # Initialize the WebDriver and store it in the context
    context.driver = webdriver.Chrome()

@when(u'Open NP Page')
def openNPpage(context):
    # Open the given URL in the browser
    context.driver.get("https://www.np.edu.sg/")
    sleep (2)

@then(u'Open NP Courses page')
def OpenCoursesPage(context):
    # Use the existing driver from the context, do not re-initialize it
    wait = WebDriverWait(context.driver, 10)
    # Locate the Courses link by its text, which is more reliable than using href attribute
    courses_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Courses")))
    # Click the Courses link
    courses_link.click()
    sleep (2)

@then(u'Open NP Part time Courses page')
def OpenParttimeCoursesPage(context):
    # Use the existing driver from the context, do not re-initialize it
    wait = WebDriverWait(context.driver, 10)
    # Locate the part time Courses link by its text, which is more reliable than using href attribute
    part_time_courses_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Part-Time Courses")))
    # Click the part time Courses link
    part_time_courses_link.click()
    window_handles = context.driver.window_handles

    # Switch to the window/tab
    context.driver.switch_to.window(window_handles[0])

    # Close the current window/tab
    context.driver.close()

    #Switch back to the original window/tab
    context.driver.switch_to.window(window_handles[1])
    sleep(2)



@then(u'Input CourseName "{courseName}"')
def fillcourseName(context, courseName):
    wait = WebDriverWait(context.driver, 20)
    # Wait for the search input field to be present in the DOM
    search_input = wait.until(EC.presence_of_element_located((By.NAME, "keyword")))
    # Clear the search input field in case there's any pre-filled text
    search_input.clear()
    # Enter the course name into the search input field
    search_input.send_keys(courseName)
    sleep (2)

@then(u'Click the search button')
def clickSearchButton(context):
    # Wait for the button to be clickable
    submit_button = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    # Click the submit button
    submit_button.click()
    sleep(2)
    context.driver.execute_script("window.scrollBy(0, 1000)")  # Scrolls down 1000 pixels
    sleep(2)
    context.driver.execute_script("window.scrollBy(0, -1000)")  # Scrolls up 1000 pixels
    sleep(2)

@then(u'Click the clear all button')
def clearAllButton(context):
    wait = WebDriverWait(context.driver, 10)
    clear_all_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Clear All")))
    clear_all_link.click()
    sleep(2)
    context.driver.execute_script("window.scrollBy(0, 1000)")  # Scrolls down 1000 pixels
    sleep(2)
    context.driver.execute_script("window.scrollBy(0, -1000)")  # Scrolls up 1000 pixels
    sleep(2)

@then(u'Click the search button for 2nd time')
def clickSearchButton(context):
    # Wait for the button to be clickable
    submit_button = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    sleep(2)
    # Click the submit button
    submit_button.click()
    sleep(2)
    context.driver.execute_script("window.scrollBy(0, 500)")  # Scrolls down 500 pixels
    sleep(2)
    context.driver.execute_script("window.scrollBy(0, -500)")  # Scrolls up 500 pixels
    sleep(2)

    
@then(u'Close browser')
def close_browser(context):
    # Close the browser
    context.driver.quit()

