from behave import step, then, given
from BDDCommon.CommonDAO.couponsDAO import CouponsDAO
from BDDCommon.CommonFuncs.webcommon import WebCommon
from BDDCommon.CommonConfigs.locatosconfig import CART_LOCATORS


@step("I verify coupon is applied successfully")
def verify_coupon_to_applied(context):
    context.execute_steps(
        """
        Given Get metadata from coupon
        And I get the total dollar amount of the cart
        then Confirmation message is displayed
        then Discount total is showed on amounts
        then Discount is applied on the total correctly
        """
    )


@step("I get the total dollar amount of the cart")
def get_total_coupon_on_cart_page(context):
    import time

    time.sleep(1)
    # Obtener WebElement de total
    total_amount = WebCommon.get_webelement_from_locators(
        context, CART_LOCATORS, "total-value"
    )
    subtotal_amount = WebCommon.get_webelement_from_locators(
        context, CART_LOCATORS, "subtotal-value"
    )

    # Obtener el texto
    total_value = WebCommon.get_element_text(total_amount)
    subtotal_value = WebCommon.get_element_text(subtotal_amount)

    # Reemplazarlo para obtener solo el valor y pasarlo al contexto
    total_value = total_value.replace("$", "")
    subtotal_value = subtotal_value.replace("$", "")

    # Define los valores como parte del contexto
    context.total_value = total_value
    context.subtotal_value = subtotal_value


@given("Get metadata from coupon")
def get_metadata_from_coupon(context):
    try:
        coupon_data = context.coupon_data
    except AttributeError as e:
        raise AssertionError(f"No se ha obtenido coupon_data desde el contexto: {e}")

    # Obtiene ID de la data del cupón
    coupon_id = coupon_data.get("id")

    coupon_metadata = CouponsDAO().get_coupon_metadata_by_id(coupon_id)

    # Pasa la metadata al contexto
    context.coupon_metadata = coupon_metadata


@then("Confirmation message is displayed")
def verify_confirmation_message(context):
    key_message_webElement = WebCommon.get_webelement_from_locators(
        context, CART_LOCATORS, "confirmation_application_coupons"
    )

    WebCommon.assert_element_visible(key_message_webElement)


@then("Discount total is showed on amounts")
def verify_discount_total(context):
    # Obtener la etiqueta de descuento
    discount_label = WebCommon.get_webelement_from_locators(
        context, CART_LOCATORS, "discount-label"
    )
    WebCommon.assert_element_visible(discount_label)

    # Obtener el total de descuento
    discount_amount = WebCommon.get_webelement_from_locators(
        context, CART_LOCATORS, "discount-value"
    )
    WebCommon.assert_element_visible(discount_amount)


@then("Discount is applied on the total correctly")
def verify_discount_applied(context):
    # Obtener la metadata
    try:
        coupon_metadata = context.coupon_metadata
        total_value = int(context.total_value)
        subtotal_value = int(context.subtotal_value)
    except AttributeError as e:
        raise AssertionError(
            f"No se ha obtenido coupon_metadata desde el contexto: {e}"
        )

    # Obtener webElement de totales parciales
    discount_amount = WebCommon.get_webelement_from_locators(
        context, CART_LOCATORS, "discount-value"
    )
    discount_text = WebCommon.get_element_text(discount_amount)
    discount_value = int(discount_text.replace("-$", ""))

    # Obtener el total de descuento
    # Obtener los montos para cada tipo
    discount_type = coupon_metadata.get("discount_type")
    discount_total = int(coupon_metadata.get("coupon_amount"))

    if discount_type == "percent":
        calculate_discount = subtotal_value * discount_total / 100
        calculate_discount = int(calculate_discount)
    else:
        calculate_discount = int(discount_total)

    # Comprobar que el descuento sea el correcto
    assert calculate_discount == discount_value, (
        "El descuento no coincide con el entregado. "
        f"Esperado: {calculate_discount} "
        f"Obtenido: {discount_value}"
    )

    # Corroborar el total de la compra
    calculate_total = subtotal_value - discount_value

    assert calculate_total == total_value, (
        "El total no coincide con el descuento aplicado. "
        f"Esperado {calculate_total} "
        f"Obtenido {total_value}"
    )
