Feature: Verify Full Time Courses page

    Background: Common Steps
        Given chrome browser is launched
        When open Full-Time Courses page

    Scenario: User searches for a business course
        Then the user inputs business and clicks on "Search" button
        And all relevant business courses will be displayed

    Scenario: User searches for a business course and resets the output
        Then the user inputs business and cicks on "Search" button
        Then the user clicks on the "Reset" button
        And the default list of courses will be displayed 

    Scenario Outline: User search for courses using the "Course clusters" dropdown
        Then the user selects multiple <courseCluster> under dropdown and clicks on "Search" button
        And all <courseCluster> courses will be displayed

    Examples:
        |courseCluster|
        |Engineering|
        |Information & Digital Technologies|




        


