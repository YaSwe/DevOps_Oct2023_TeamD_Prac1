from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


@when(u'open Full-Time Courses page')
def openFullTimeCoursesPage(context):
    context.driver.get("https://www.np.edu.sg/schools-courses/full-time-courses")
    context.driver.maximize_window()


@then(u'the user inputs {searchInput} and clicks on "Search" button')
def inputCourseAndSubmit(context, searchInput):
    context.driver.find_element(By.XPATH, '//*[@id="courseListingSearch"]').send_keys(searchInput)
    sleep(3)

    context.driver.find_element(By.XPATH, '//*[@id="btn-search"]').click()
    sleep(3)


@then(u'all relevant {searchInput} courses will be displayed')
def verifyCoursesResults(context, searchInput):
    course_titles = []
    courses = context.driver.find_elements(By.XPATH, '//*[@id="courseListingData"]/div/div/div[1]')

    for course in courses:
        course_title = course.find_element(By.XPATH, '//*[@id="courseListingData"]/div/div/div[1]/div/a/h3').text
        course_titles.append(course_title)

    for course_title in course_titles:
        assert searchInput in course_title.lower()
    sleep(3)


@then(u'the user inputs {searchInput} and cicks on "Search" button')
def inputSearchAndSubmit(context, searchInput):
    context.driver.find_element(By.XPATH, '//*[@id="courseListingSearch"]').send_keys(searchInput)
    sleep(3)

    context.driver.find_element(By.XPATH, '//*[@id="btn-search"]').click()
    sleep(3)


@then(u'the user clicks on the "Reset" button')
def clickResetButton(context):
    context.driver.find_element(By.XPATH, '//*[@id="btn-reset"]').click()
    sleep(3)


@then(u'the default list of courses will be displayed')
def verifyDefaultCourses(context):
    assert context.driver.find_element(By.XPATH, '/html/body/main/section/div/div[2]/div[2]/div').text == 'Displaying 1 - 9 of 41 courses'
    sleep(3)


@then(u'the user selects multiple {course} under dropdown and clicks on "Search" button')
def selectDropdownSelection(context, course):
    dropdown_element = context.driver.find_element(By.XPATH, '//*[@id="courseListingInterest"]')
    select = Select(dropdown_element)
    select.select_by_visible_text(f"{course}")
    sleep(3)

    context.driver.find_element(By.XPATH, '//*[@id="btn-search"]').click()
    sleep(3)


@then(u'all {courseName} courses will be displayed')
def verifyCourses(context, courseName):
    course_clusters = []
    courses = context.driver.find_elements(By.XPATH, '//*[@id="courseListingData"]/div/div/div[1]')

    for course in courses:
        course_cluster = course.find_element(By.XPATH, '//*[@id="courseListingData"]/div/div/div[2]/div/div[2]/a').text
        course_clusters.append(course_cluster)

    for course_cluster in course_clusters:
        assert courseName in course_cluster
    
    sleep(3)
