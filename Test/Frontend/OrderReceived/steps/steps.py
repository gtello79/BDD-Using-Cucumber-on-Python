from behave import step, then
from BDDCommon.CommonConfigs.locatosconfig import ORDER_RECEIVED_LOCATORS
from BDDCommon.CommonFuncs.webcommon import WebCommon


@step("order confirmation page should load with correct data")
def order_confirmation_loaded(context):
    # Verifica la URL actual sea la correcta
    #WebCommon.assert_include_text_into_url(context, "checkout/order-received/")

    context.execute_steps(
        """
            then Order received header should be displayed
            then Order received message should be displayed
            then verify order number and label is displayed
            then verify order date and label is displayed
            then verify order total and label is displayed
        """
    )


@then("Order received header should be displayed")
def confirmation_header_order_received(context):
    # Obtiene el locator del titulo y verifica que el titulo sea correcto
    order_received_header = WebCommon.get_webelement_from_locators(
        context, ORDER_RECEIVED_LOCATORS, "order-received-header"
    )
    WebCommon.assert_validate_text(order_received_header, "Order received")


@then("Order received message should be displayed")
def confirmation_thanks_message_order_received(context):
    # Obtiene el locator del mensaje de confirmación y verifica que el mensaje sea correcto
    confirmation_message_web_element = WebCommon.get_webelement_from_locators(
        context, ORDER_RECEIVED_LOCATORS, "confirmation-message"
    )

    confirmation_message_str = "Thank you. Your order has been received."
    WebCommon.assert_validate_text(
        confirmation_message_web_element, confirmation_message_str
    )


@then("verify order {field} and label is displayed")
def verify_order_number_label(context, field):
    if field == "number":
        locator = "order_number"
        expected_label = "ORDER NUMBER:"
    elif field == "date":
        locator = "order_date"
        expected_label = "DATE:"
    elif field == "total":
        locator = "order_total"
        expected_label = "TOTAL:"
    else:
        raise AssertionError(f"El campo {field} no es un campo válido")

    # Obtiene el locator del numero de orden
    order_received_web_element = WebCommon.get_webelement_from_locators(
        context, ORDER_RECEIVED_LOCATORS, locator
    )

    # Obtener el string asociado al locator
    order_received_str = order_received_web_element.text

    # Ahora, hay que obtener el numero de orden de la base de datos
    try:
        label_ordernumber, order_number = order_received_str.split("\n")
    except ValueError:
        raise AssertionError("El valor obtenido no corresponde a un número")

    assert (
        label_ordernumber == expected_label
    ), f'Expected label is "{expected_label}" but got {label_ordernumber}'

    try:
        context.order_context
    except AttributeError:
        context.order_context = {}

    context.order_context[locator] = order_number
