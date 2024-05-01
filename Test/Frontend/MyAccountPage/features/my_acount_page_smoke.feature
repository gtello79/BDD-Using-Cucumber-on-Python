Feature: My account Smoke Test

    Feature Description

    Scenario: Valid user should be to login

        Given I go to 'my account' page
        When I type 'pruebasgtv355@gmail.com' into username of login form
        And I type 'B)dsbRhv4wQIA!i*1#j91i*3' into password of login form
        And I click on the 'login' button
        Then User should b logged in

    Scenario: User with wrong password should get correct error message

        Given I go to 'my account' page
        When I type 'pruebasgtv355@gmail.com' into username of login form
        And I type 'wrong_password' into password of login form
        And I click on the 'login' button
        Then I get a error message with the email 'pruebasgtv355@gmail.com' should be displayed



    """
    # Esta es la alternativa para abarcar diferentes tipos de errores con un solo Scenario
    Scenario Outline: User with <type_error> should get correct error message
        Given I go to 'my account' page
        When I type '<email>' into username of login form
        And I type '<password>' into password of login form
        And I click on the 'login' button
        Then I get a <type_error> message with the email '<email>' should be displayed

        Examples:
            | type_error         | email                   | password       |
            | wrong password     | pruebasgtv355@gmail.com | wrong_password |
            | non-existing email | bad355@gmail.com        | wrong_password |
    """