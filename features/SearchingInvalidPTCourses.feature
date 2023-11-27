Feature: Verifying search for Invalid Part Time Course

    Background: Common Steps
        Given Chrome browser is Launched
        When Open NP Page
        Then Open NP Courses page
        Then Open NP Part time Courses page

    Scenario: Searching invalid part time course and clear search bar
        Then Input CourseName "abcdefg"
        Then Click the search button for 2nd time
        Then Click the clear all button
        And Close browser

    
