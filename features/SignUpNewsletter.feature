Feature: Verify Sign-Up Newsletter

    Background: Common Steps
        Given chrome browser is launched
        When open home page

    Scenario: User inputs email and subscribes to the newsletter
        Then the user inputs example@gmail.com as email and clicks on "Sign up" button
        And the user successfully subscribed to the newsletter

    Scenario: User inputs incorrect email
        Then the user inputs example and clicks on "Sign up" button
        And an error message will be displayed

