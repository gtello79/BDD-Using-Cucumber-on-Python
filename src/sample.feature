Feature: Login as valid user
	Scenario: Login as an existing user in

		Given I go to login page
	    When I login with my credentials
		Then I should see the next "Welcome" and my full name
		And I logout