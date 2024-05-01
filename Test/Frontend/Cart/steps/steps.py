from logging import raiseExceptions
from behave import step
from BDDCommon.CommonConfigs.locatosconfig import CART_LOCATORS
from BDDCommon.CommonFuncs.webcommon import WebCommon


@step("I select '{field_option}' option")
def select_shipping_option(context, field_option):
    available_fields = ["free-shipping", "local-pickup", 'add-a-coupon']
    if field_option not in available_fields:
        raise raiseExceptions(
            f"El campo {field_option} no está dentro de las opciones disponibles"
            f"Opciones: {available_fields}"
        )

    key = f"{field_option}-option"

    # Get webElement associate to the field_option
    free_shipping_webElement = WebCommon.get_webelement_from_locators(
        context, CART_LOCATORS, key
    )

    # Make click on the web Element
    WebCommon.click_element(free_shipping_webElement)

    # Verifica si el campo esta seleccionado
    WebCommon.assert_radio_button_is_selected(free_shipping_webElement)

@step('Applied a discount coupon on the Cart')
def applied_discount_coupon_on_the_cart(context):
    pass