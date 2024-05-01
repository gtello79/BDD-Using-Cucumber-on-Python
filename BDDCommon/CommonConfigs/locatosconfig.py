from selenium.webdriver.common.by import By


LOCATORS = {
    "login_form": {"type": By.XPATH, "locator": "//form[1]"},
    "user field": {"type": By.ID, "locator": "id_email"},
    "password field": {"type": By.ID, "locator": "id_password"},
}

MY_ACCOUNT_LOCATORS = {
    # Loggin form
    "login_user_name": {"type": By.ID, "locator": "username"},
    "login_password": {"type": By.ID, "locator": "password"},
    "login_button": {"type": By.CSS_SELECTOR, "locator": 'button[name="login"]'},
    # Registration form
    "reg_email": {"type": By.ID, "locator": "reg_email"},
    "reg_password": {"type": By.ID, "locator": "reg_password"},
    # User logged on her count
    "user_nave_bar": {
        "type": By.CSS_SELECTOR,
        "locator": "div.entry-content nav.woocommerce-MyAccount-navigation",
    },
    "user_nave_bar_logout": {
        "type": By.CSS_SELECTOR,
        "locator": "div.entry-content nav.woocommerce-MyAccount-navigation ul li:nth-of-type(6)",
    },
    # User errors
    "error_box": {"type": By.CSS_SELECTOR, "locator": "ul.woocommerce-error"},
    "login_bad_password_msg": {
        "type": By.CSS_SELECTOR,
        "locator": "ul.woocommerce-error li:nth-of-type(1)",
    },
}

NAV_BAR_LOCATORS = {
    "side_cart": {"type": By.CSS_SELECTOR, "locator": "ul#site-header-cart"}
}

MY_HOME_LOCATORS = {
    # Shop List
    "products-list-on-sell": {
        "type": By.CSS_SELECTOR,
        "locator": "div#primary ul.products li.product a.add_to_cart_button.ajax_add_to_cart",
    }
}

CART_LOCATORS = {
    "shipping-content": {
        "type": By.CSS_SELECTOR,
        "locator": "div.wc-block-components-totals-shipping",
    },
    # Shipping types options
    "free-shipping-option": {
        "type": By.CSS_SELECTOR,
        "locator": "#radio-control-0-free_shipping\\:4",
    },
    "local-pickup-option": {
        "type": By.CSS_SELECTOR,
        "locator": "#radio-control-0-local_pickup\:5",
    },
    # Proceed checkout button
    "checkout-button": {
        "type": By.CSS_SELECTOR,
        "locator": "span.wc-block-components-button__text",
    },

    # Coupons section
    "add-a-coupon-button": {
        "type": By.CSS_SELECTOR,
        "locator": "div.wc-block-components-totals-coupon a.wc-block-components-totals-coupon-link",
    },
    "coupon_code_index": {
        "type": By.ID,
        "locator": "wc-block-components-totals-coupon__input-0",
    },
    "apply-coupon-button": {
        "type": By.CSS_SELECTOR,
        "locator": "#wc-block-components-totals-coupon__form > button > span",
    },
    'confirmation_application_coupons':{
        'type': By.CSS_SELECTOR,
        'locator': 'div.wc-block-components-notice-banner__content'
    },

    # Discount Section
    'discount_value':{
        'type': By.CSS_SELECTOR,
        'locator': 'span.wc-block-formatted-money-amount.wc-block-components-formatted-money-amount.wc-block-components-totals-item__value'
    },

    # Total section
    'total-value':{
        'type': By.CSS_SELECTOR,
        'locator': 'div.wc-block-components-totals-item__value'
    },
    'subtotal-value':{
        'type': By.CSS_SELECTOR,
        'locator': 'div.wp-block-woocommerce-cart-order-summary-subtotal-block span.wc-block-components-totals-item__value '
    },
    'discount-value':{
        'type': By.CSS_SELECTOR,
        'locator': 'div.wc-block-components-totals-discount span.wc-block-components-totals-item__value'
    },
    'discount-label':{
        'type': By.CSS_SELECTOR,
        'locator': 'div.wc-block-components-totals-discount span.wc-block-components-totals-item__label'
    }
}


CHECKOUT_LOCATORS = {
    "checkout-header": {
        "type": By.CSS_SELECTOR,
        "locator": "header.entry-header h1.entry-title",
    },
    "checkout-form": {
        "type": By.CSS_SELECTOR,
        "locator": "form.wc-block-components-form.wc-block-checkout__form",
    },
    # Field forms locators
    "form-input-email": {"type": By.ID, "locator": "email"},
    "form-input-first_name": {"type": By.ID, "locator": "shipping-first_name"},
    "form-input-last_name": {"type": By.ID, "locator": "shipping-last_name"},
    "form-input-address-1": {"type": By.ID, "locator": "shipping-address_1"},
    "form-input-address-2": {"type": By.ID, "locator": "shipping-address_2"},
    "form-input-country": {"type": By.ID, "locator": "components-form-token-input-0"},
    "form-input-shipping-city": {"type": By.ID, "locator": "shipping-city"},
    "form-input-region": {"type": By.ID, "locator": "components-form-token-input-1"},
    "form-input-phone": {"type": By.ID, "locator": "shipping-phone"},
    # Place Order Button
    "button-place-order": {
        "type": By.CSS_SELECTOR,
        "locator": "button.components-button.wc-block-components-button.wp-element-button.wc-block-components-checkout-place-order-button.contained",
    },
}


ORDER_RECEIVED_LOCATORS = {
    "order-received-header": {
        "type": By.CSS_SELECTOR,
        "locator": "header.entry-header h1.entry-title",
    },
    "confirmation-message": {
        "type": By.CSS_SELECTOR,
        "locator": "div.woocommerce-order p.woocommerce-notice.woocommerce-notice--success.woocommerce-thankyou-order-received",
    },
    "order_number": {
        "type": By.CSS_SELECTOR,
        "locator": "div.woocommerce-order li.woocommerce-order-overview__order",
    },
    "order_date": {
        "type": By.CSS_SELECTOR,
        "locator": "div.woocommerce-order li.woocommerce-order-overview__date",
    },
    "order_total": {
        "type": By.CSS_SELECTOR,
        "locator": "div.woocommerce-order li.woocommerce-order-overview__total",
    },
}
