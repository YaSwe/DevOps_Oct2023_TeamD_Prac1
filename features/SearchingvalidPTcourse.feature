Feature: Verifying PT course search is valid

    Background: Common Steps
        Given Chrome browser is Launched
        When Open NP Page
        Then Open NP Courses page
        Then Open NP Part time Courses page
        
    Scenario: Searching valid part time course
        Then Input CourseName "IT"
        Then Click the search button
        And Close browser