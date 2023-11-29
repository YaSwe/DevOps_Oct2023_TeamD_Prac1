Feature: Verify NP Website Search Bar is valid

    Background: Common Steps
        Given   Chrome brower is Launched
        When    Open NP page

    Scenario: Search for Diploma on Information Technology
        Then    Input Search "Information Technology"
        And     Close browser

    Scenario: Search for Enrolment Criteria
        Then    Search for Enrolment Criteria
        And     Close browser