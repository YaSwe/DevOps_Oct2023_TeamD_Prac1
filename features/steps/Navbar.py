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
        
@then(u'Verify Navigation bar is visible')
def verify_navbar_visibility(context):
    navbar = context.driver.find_element(By.ID, 'navbarNavDropdown')
    assert navbar.is_displayed(), "Navigation bar is not visible"

@then(u'Close browser')
def CloseBrowser(context):
    context.driver.close()


@then(u'Verify Dropdown menu in navigation bar is visible')
def hover_over_navbar(context):
    navbar_links_xpath = [
        '//*[@id="navbarNavDropdown"]/ul/li[1]',
        '//*[@id="navbarNavDropdown"]/ul/li[2]',
        '//*[@id="navbarNavDropdown"]/ul/li[3]',
        '//*[@id="navbarNavDropdown"]/ul/li[4]',
        '//*[@id="navbarNavDropdown"]/ul/li[5]',
        '//*[@id="navbarNavDropdown"]/ul/li[6]',
        '//*[@id="navbarNavDropdown"]/ul/li[7]'
    ]

    for xpath in navbar_links_xpath:
        navbar_link = context.driver.find_element(By.XPATH, xpath)
        ActionChains(context.driver).move_to_element(navbar_link).perform()
        sleep(1)  # Adjust as necessary for any additional visual confirmation
        dropdown_menu = context.driver.find_element(By.XPATH, f'{xpath}/div')
        assert dropdown_menu.is_displayed(), "dropdown menu is not visible"

        

@then(u'Click Student Life link in the navigation bar')
def click_nav_links(context):
    navbar_links_xpath = [
        '//*[@id="navbarNavDropdown"]/ul/li[4]',
    ]

    for xpath in navbar_links_xpath:
        link = context.driver.find_element(By.XPATH, xpath)
        link.click()
        sleep(2)  # Allow time for the page to load, adjust as necessary
        # Get the current URL and assert that it's a new page
        current_url = context.driver.current_url
        expected_url = "https://www.np.edu.sg/student-life/experience-your-xtraordinary"
        assert current_url == expected_url, "Student Life link does not navigate to the correct page"
        context.driver.back()  # Go back to the main page for the next iteration


@then(u'Check all links are valid in AboutNP page')
def check_all_options(context):
    navbar_links_xpath = [
        '//*[@id="navbarNavDropdown"]/ul/li[1]',
        '//*[@id="navbarNavDropdown"]/ul/li[2]',
        '//*[@id="navbarNavDropdown"]/ul/li[3]',
        '//*[@id="navbarNavDropdown"]/ul/li[4]',
        '//*[@id="navbarNavDropdown"]/ul/li[5]',
        '//*[@id="navbarNavDropdown"]/ul/li[6]',
        '//*[@id="navbarNavDropdown"]/ul/li[7]'
    ]

    for xpath in navbar_links_xpath:
        link_of_list = []
        navbar_link = context.driver.find_element(By.XPATH, xpath)
        ActionChains(context.driver).move_to_element(navbar_link).perform()

        # Verifying if Dropdown menu is visible
        current_url = context.driver.current_url
        new_url = context.driver.current_url
        NumberOfMainLinks = context.driver.find_elements(By.XPATH, f'{xpath}/div/div/div/div[2]/div/div')
        Number1 = len(NumberOfMainLinks)

        for i, _ in enumerate(range(Number1), start=1):
            main_link = f"{xpath}/div/div/div/div[2]/div/div[{i}]/a"
            link_of_list.append(main_link)
            NumberOfSubLinks = context.driver.find_elements(By.XPATH, f'{main_link}/../ul/li')
            Number2 = len(NumberOfSubLinks)
            if Number2 != 0:
                for k, _ in enumerate(range(Number2), start=1):
                    link2 = f'{main_link}/../ul/li[{k}]/a'
                    link_of_list.append(link2)

        for links in link_of_list:
            navbar_link = context.driver.find_element(By.XPATH, xpath)
            ActionChains(context.driver).move_to_element(navbar_link).perform()
            

            # Scroll to the link to make it visible
            link_to_validate = context.driver.find_element(By.XPATH, links)
            # Get the Y coordinate of the link
            link_y = link_to_validate.location['y']
            # Calculate the middle of the screen
            middle_of_screen = context.driver.execute_script("return window.innerHeight / 2")
            # Calculate the scroll offset to position the link in the middle of the screen
            scroll_offset = link_y - middle_of_screen
            # Scroll to the link with the calculated offset
            context.driver.execute_script(f"window.scrollBy(0, {scroll_offset});")
            if scroll_offset > 328:
                sleep(1)
            link_to_validate = context.driver.find_element(By.XPATH, links)
            print(f"Scrolled to link: {links}")  # SEE STATUS
            
            last_visited = link_to_validate.get_attribute("href")
            
            # Check if the link opens in a new tab
            opens_in_new_tab = link_to_validate.get_attribute("target")
            print(opens_in_new_tab)
            if opens_in_new_tab == "_blank":
                # Open the link in a new tab using the Ctrl+Click keyboard shortcut
                link_to_validate.click()
                # Switch to the new tab
                
                context.driver.switch_to.window(context.driver.window_handles[1])
                # Wait for the new tab to load
                WebDriverWait(context.driver, 10).until(EC.url_changes(new_url))
                # Close the new tab
                context.driver.close()
                # Switch back to the original tab
                context.driver.switch_to.window(context.driver.window_handles[0])
                sleep(3)
                # Ensure focus is on the original tab
                context.driver.switch_to.default_content()
                sleep(3)
                
            else:
                # Click the link in the current tab
                link_to_validate.click()
                WebDriverWait(context.driver, 10).until(EC.staleness_of(link_to_validate))
                new_url = context.driver.current_url
                
                context.driver.back()
                
            # Add a print statement to see the status after each iteration
            print(f"Last visited processed link: {last_visited}")
            assert new_url != current_url, f"Link '{last_visited}' does not navigate to a new page because it is '{new_url}'"  # Verify that it brings you to a new page
            context.driver.execute_script("window.scrollTo(0, 0);")
            sleep(1)
        