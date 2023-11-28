from behave import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u'Chromebrowser is launched')
def launchChromeBrowser(context):
    context.driver =  webdriver.Chrome()


@when(u'Open Ngee Ann Polytechnic page')
def OpenNgeeAnnpage(context):
    context.driver.get("https://np.edu.sg/home")
    #context.driver.execute_script("document.body.style.zoom = '60%'");
    #sleep(3)
    #IDK How to make the zoom work its so weird if i make use of zoom I can reduce the number of codes needed to write
    
    
@then(u'Verify Navigation bar is visible')
def verify_navbar_visibility(context):
    navbar = context.driver.find_element(By.ID, 'navbarNavDropdown')
    assert navbar.is_displayed(), "Navigation bar is not visible"

@then(u'Close browser')
def CloseBrowser(context):
    context.driver.close()


@then(u'Check all social media links are valid in AboutNP page')
def checkSocialMedia(context):
    # XPaths for social media links in the 1st bar
    first_bar_xpaths = [
        "/html/body/main/section[4]/div/div/a[1]",
        "/html/body/main/section[4]/div/div/a[2]",
        "/html/body/main/section[4]/div/div/a[3]",
        "/html/body/main/section[4]/div/div/a[4]",
        "/html/body/main/section[4]/div/div/a[5]",
        "/html/body/main/section[4]/div/div/a[6]",
    ]
    
    # XPaths for social media links in the 2nd bar
    second_bar_xpaths = [
        "/html/body/footer/div[1]/div/div[4]/div[2]/ul/li[1]/a",
        "/html/body/footer/div[1]/div/div[4]/div[2]/ul/li[2]/a",
        "/html/body/footer/div[1]/div/div[4]/div[2]/ul/li[3]/a",
        "/html/body/footer/div[1]/div/div[4]/div[2]/ul/li[4]/a",
        "/html/body/footer/div[1]/div/div[4]/div[2]/ul/li[5]/a",
        "/html/body/footer/div[1]/div/div[4]/div[2]/ul/li[6]/a",
    ]
    

    expected_url = [
        "https://www.tiktok.com/@ngeeannpoly",
        "https://www.instagram.com/ngeeannpoly/",
        "https://www.youtube.com/user/NgeeAnnPolytechnic",
        "https://www.facebook.com/ngeeannpoly",
        "https://sg.linkedin.com/school/ngee-ann-polytechnic/",
        "https://t.me/ngeeannpoly"
    ]

    # Click on each link and verify that each pair goes to the same page
    for first_xpath, second_xpath, expect in zip(first_bar_xpaths, second_bar_xpaths, expected_url):
        first_bar_link = context.driver.find_element(By.XPATH, first_xpath)
        second_bar_link = context.driver.find_element(By.XPATH, second_xpath)

        # Click on the first link (open in a new tab)
        first_bar_link.send_keys(Keys.CONTROL + Keys.RETURN)

        # Switch to the newly opened tab
        context.driver.switch_to.window(context.driver.window_handles[1])

        # Get the current URL after clicking the first link
        first_page_url = context.driver.current_url
        sleep(1)
        # Close the tab
        context.driver.close()

        # Switch back to the original tab
        context.driver.switch_to.window(context.driver.window_handles[0])

        # Click on the second link (open in a new tab)
        second_bar_link.send_keys(Keys.CONTROL + Keys.RETURN)

        # Switch to the newly opened tab
        context.driver.switch_to.window(context.driver.window_handles[1])

        # Get the current URL after clicking the second link
        second_page_url = context.driver.current_url
        sleep(1)
        # Close the tab
        context.driver.close()

        # Switch back to the original tab
        context.driver.switch_to.window(context.driver.window_handles[0])

        # Verify that both links lead to the same page
        assert first_page_url == second_page_url, f"Links {first_bar_link} and {second_bar_link} do not lead to the same page"
        assert first_page_url == expect, f"Compared link: {first_page_url} do not lead to the expected URL:{expect}"


