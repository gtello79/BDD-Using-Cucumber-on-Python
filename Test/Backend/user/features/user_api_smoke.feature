Feature: Test for manage a user on the API

    Scenario: Verify 'POST /customer' create user

        Given I generate random email and password
        When I call 'create customer' API
        Then Customer should be created

        