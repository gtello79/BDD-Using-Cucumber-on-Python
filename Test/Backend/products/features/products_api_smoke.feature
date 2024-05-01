Feature: Product API Smoke

    Feature Description

    Scenario: Verify 'get all products' returns the expected number of products

        Given I get number of available products from db
        When I get number of available products from api
        Then the total products number in api should be same as in db

    Scenario: Verify 'products/id' returns a products with the given id

        Given I get 1 random product from database
        Then I verify the product api returns correct product by id