Feature: Order Placement

    Scenario: New user place order with 1 item without creating an account

        Given I go to 'home' page
        When I add 3 random item to cart from the homepage
        And I click on cart in the top nav bar and verify cart page opens
        And I select 'free-shipping' option
        And I click on 'Proceed to checkout' button in the cart page
        And I verify 'Checkout' page is loaded
        And I fill in the billing details form
        And I click on 'Place order' button in the checkout page
        Then order confirmation page should load with correct data
        Then I verify order is created in database

    @coupon
    Scenario: Apply coupons over cart

        Given I go to 'home' page
        And I create a coupon with given parameters
            """
            {
            "discount_type": "percent",
            "amount": "50",
            "individual_use": "false",
            "usage_count":10,
            "usage_limit":5,
            "exclude_sale_items": "false"
            }
            """
        When I add 3 random item to cart from the homepage
        And I click on cart in the top nav bar and verify cart page opens
        And I select 'free-shipping' option
        And I click on 'Add a coupon' button in the cart page
        And I apply the coupon in the cart page
        And I click on 'Apply' button in the cart page
        Then I verify coupon is applied successfully