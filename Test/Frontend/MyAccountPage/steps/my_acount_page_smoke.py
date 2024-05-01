from behave import when, then, step
from BDDCommon.CommonSteps.webstepscommon import *
from BDDCommon.CommonFuncs.webcommon import WebCommon
from BDDCommon.CommonConfigs.locatosconfig import MY_ACCOUNT_LOCATORS


@when("I type '{value}' into {field} of {form_name} form")
def type_value_in_form(context, value, field, form_name):
    if field == "username":
        # Locators of login_user_name
        key = "login_user_name"
    elif field == "password":
        # Locators of login_user_password
        key = '"login_password"'
    else:
        raise Exception(f"The field {field} is not founded on the step")

    field_form_webElement = WebCommon.get_web_element_from_context(
        context, MY_ACCOUNT_LOCATORS, key
    )

    WebCommon.type_element(field_form_webElement, value)


@when("I click on the '{type}' button")
def press_a_button_by_type(context, type):
    # Get the type button
    if type == "login":
        key = "login_button"
    else:
        raise Exception(f"The button {type} is not founded on the step")

    select_btn_webdriver = WebCommon.get_webelement_from_locators(
        context, MY_ACCOUNT_LOCATORS, key
    )

    WebCommon.click_element(select_btn_webdriver)


@step("User should b logged in")
def the_user_should_be_logged(context):
    elements_to_verify = ["user_nave_bar", "user_nave_bar_logout"]

    for locator_element in elements_to_verify:
        # Verify the nav_bar_situation

        element_base_webElement = WebCommon.get_webelement_from_locators(
            context, MY_ACCOUNT_LOCATORS, locator_element
        )

        WebCommon.assert_element_visible(element_base_webElement)


@then("I get a {type_error} message with the email '{email}' should be displayed")
def message_error_should_be_displayed(context, email, type_error):
    # Validate exposition of error content box

    message_error_webElement = WebCommon.get_webelement_from_locators(
            context, MY_ACCOUNT_LOCATORS, "error_box"
        )

    WebCommon.assert_element_visible(message_error_webElement)

    logger.info("Se ha encontrado la caja asociada a la presentación del error")

    if type_error in ("wrong password", "error"):
        expected_message_error = "Error: The password you entered for the email address pruebasgtv355@gmail.com is incorrect. Lost your password?"
    elif type_error == "non-existing email":
        expected_message_error = (
            "Unknown email address. Check again or try your username."
        )

    WebCommon.assert_validate_text(
        context_or_web_element=message_error_webElement,
        expected_text=expected_message_error,
    )

    logger.info("Se ha validado el mensaje correcto")
