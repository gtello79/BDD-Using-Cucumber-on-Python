Feature: Pasando Data mediante linea de comando

    Scenario: User Loggin successfully

        Given I create a new User
        When I type email
        When I type password
        When I click on 'Login'
        Then I should see the text Welcome
