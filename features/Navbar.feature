Feature: Verify the workings of Ngee Ann Polytechnic Navbar

    Scenario: Check Ngee Ann Polytechnic navbar
        Given   Chromebrowser is launched
        When    Open Ngee Ann Polytechnic page
        Then    Verify Navigation bar is visible
        Then    Verify Dropdown menu in navigation bar is visible
        Then    Click Student Life link in the navigation bar
        And     Check all links are valid in AboutNP page




