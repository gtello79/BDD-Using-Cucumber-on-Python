Feature: Create coupon smoke

    Scenario Outline: Create coupon with minimum parameters should create coupon
        Given I create a "<discount_type>" coupon
        Then the coupon should existe in database

        Examples:
            | discount_type |
            | None          |
            | percent       |
            | fixed_cart    |
            | fixed_product |

    Scenario: Verfiy the given coupon metadata are recorded correctly
        Given I create a coupon with given parameters
            """
            {
            "discount_type": "fixed_cart",
            "amount": "50",
            "individual_use": "false",
            "usage_count":10,
            "usage_limit":5,
            "exclude_sale_items": "True"
            }
            """
        Then Verify the given coupon metadata are recorded correctly