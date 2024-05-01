from tkinter import W
from behave import then, step, given
from BDDCommon.CommonFuncs.webcommon import WebCommon
from BDDCommon.CommonConfigs.locatosconfig import (
    LOCATORS,
    NAV_BAR_LOCATORS,
    CHECKOUT_LOCATORS,
    CART_LOCATORS,
)

from BDDCommon.CommonHelpers.UtilitiesHelpers import (
    generate_random_user_and_password,
    generate_random_name_and_last_name,
)
import logging as logger
import time


# Start of step definition
@step("I go to '{site}' page")
@given("I go to the site '{site}'")
def go_to_a_site(context, site):
    """
    Step definition to go to a specific url
    """
    logger.info(f"NAVEGANDO HACIA EL SITIO {site}")
    WebCommon.go_to_url(context, site)
    context.field = {}


@then("The page title should be {expected_title}")
def verify_homepage_title(context, expected_title):
    WebCommon.assert_page_title(context, expected_title)


@then('Verify url should be "{expected_url}"')
def verify_homepage_url(context, expected_url):
    """
    Verifies the currents urls is a expected urls
    """

    WebCommon.assert_current_url(context, expected_url)


@then('The "{state}" should be a value')
def example_scenario_outline(context, state):
    print(f"My Current status es {state}")


@then('Get "{field}" field on the form')
def get_field_by_form(context, field):
    try:
        search_field = LOCATORS[field]
    except KeyError:
        Exception(f"El campo {field} no se encuentra dentro del archivo Locators")

    context.field["field"] = search_field


@step("I click on cart in the top nav bar and verify cart page opens")
def access_to_cart_page_from_nav_bar(context):
    # Selecciona el elemento del menu despegable
    # Obtener el webElement de site_cart
    site_cart_webElement = WebCommon.get_webelement_from_locators(
        context, NAV_BAR_LOCATORS, "side_cart"
    )

    # Ejemplo para realizar onMouseOver sobre el webElement
    WebCommon.make_hover_on_a_element(context, site_cart_webElement)

    # Clickear WebElement
    WebCommon.click_element(context_or_web_element=site_cart_webElement)


@step("I verify '{site}' page is loaded")
def verify_that_the_page_is_loaded(context, site):
    site_locators = {}

    # Get the locators on function of the site
    if site.lower() == "checkout":
        site_locators = CHECKOUT_LOCATORS
        to_check_fields = ["checkout-header", "checkout-form"]
    else:
        raise Exception(
            f"No se ha encontrado un sitio para {site}. Favor configurarlo en verificacion"
        )

    for field in to_check_fields:
        # Obtain the valor for type and locator on the Header
        site_element_webElement = WebCommon.get_webelement_from_locators(
            context, site_locators, field
        )

        if "header" in field:
            WebCommon.assert_validate_text(site_element_webElement, "Checkout")

        WebCommon.assert_element_visible(site_element_webElement)


@step("I fill in the {form_name} form")
def fill_form_field(context, form_name):
    if form_name == "billing details":
        CHECKOUT_LOCATORS_KEYS = list(CHECKOUT_LOCATORS.keys())

        # Obtiene solo los campos del formulario
        available_field_forms = [
            key for key in CHECKOUT_LOCATORS_KEYS if key.startswith("form-input")
        ]

    else:
        raise Exception(
            f"No se ha encontrado un formulario para {form_name}. Favor configurarlo en verificacion"
        )

    # Por cada campo listado, escribe información de acuerdo a su valor
    for field_name in available_field_forms:
        # Obtener el webElement de site_cart
        field_webdriver = WebCommon.get_webelement_from_locators(
            context, CHECKOUT_LOCATORS, field_name
        )

        text_to_write = ""
        if field_name.endswith("email"):
            random_gen = generate_random_user_and_password()

            text_to_write = random_gen["email"]
        elif field_name.endswith("first_name") or field_name.endswith("last_name"):
            random_gen = generate_random_name_and_last_name()

            if field_name.endswith("first_name"):
                key = "first_name"
            elif field_name.endswith("last_name"):
                key = "last_name"
            text_to_write = random_gen[key]

        elif field_name.endswith("address-1") or field_name.endswith("address-2"):
            text_to_write = "Santa Victoria 387"

        elif field_name.endswith("shipping-city"):
            text_to_write = "Santiago"

        elif field_name.endswith("country"):
            text_to_write = "Chile"

        elif field_name.endswith("region"):
            text_to_write = "Región Metropolitana de Santiago"
        # Si se ha pasado un valor, se escribe
        if text_to_write:
            WebCommon.type_element(field_webdriver, text_to_write)

    # 4 segundos por si es necesario procesar la información del formulario
    time.sleep(4)


@step("I click on '{message_button}' button in the {site} page")
def make_click_on_message_button(context, message_button, site):
    if site == "cart":
        if message_button == "Proceed to checkout":
            locators_dict = CART_LOCATORS
            button_key = "checkout-button"
        elif message_button == "Add a coupon":
            locators_dict = CART_LOCATORS
            button_key = "add-a-coupon-button"
        elif message_button == "Apply":
            locators_dict = CART_LOCATORS
            button_key = "apply-coupon-button"

    elif site == "checkout" and message_button == "Place order":
        locators_dict = CHECKOUT_LOCATORS
        button_key = "button-place-order"

    select_btn_webdriver = WebCommon.get_webelement_from_locators(
        context, locators_dict, button_key
    )

    WebCommon.click_element(select_btn_webdriver)

    if site == "checkout" and message_button == "Place order":
        time.sleep(5)


@step("I apply the coupon in the {site} page")
def apply_coupon_on_the_site(context, site):
    # Get the coupon code
    try:
        coupon_code = context.coupon_data.get("code")
    except AttributeError as e:
        logger.error(f"Error: {e}")
        raise AssertionError(
            "No se ha entregado la data correspondiente al coupon, verificar contexto"
        )
    except KeyError as e:
        logger.error(f"Error: {e}")
        raise AssertionError(
            "No se ha entregado la data correspondiente al coupon, verificar contexto"
        )

    # Obtener el webElement de site_cart
    add_coupon_webElement = WebCommon.get_webelement_from_locators(
        context, CART_LOCATORS, "coupon_code_index"
    )

    # Clickear WebElement
    WebCommon.type_element(
        context_or_web_element=add_coupon_webElement, input_string=coupon_code
    )

