Feature: Pasando string from steps

    Scenario: Scenario 1 of Feature 1

        Given I am a passing steps
            """
            This is just random string in 1st step
            Second line of 1st string. And
            3rd line of 1st string
            """
        Then I another a passing step
