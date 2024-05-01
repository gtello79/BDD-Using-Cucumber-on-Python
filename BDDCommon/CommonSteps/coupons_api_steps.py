from behave import step, then, given
import logging as logger
import json
from BDDCommon.CommonHelpers.UtilitiesHelpers import generate_random_coupon_code
from BDDCommon.CommonAPI.coupons_api import CouponsAPI
from BDDCommon.CommonDAO.couponsDAO import CouponsDAO


@step('I create a "{discount_type}" coupon')
def create_a_coupon_with_given_discount_type(context, discount_type):
    print(f"Discount type: {discount_type}")
    data = {
        "code": generate_random_coupon_code(),
    }

    if discount_type.lower() != "none":
        data["discount_type"] = discount_type
        context.discount_type = discount_type
    else:
        context.discount_type = "fixed_cart"

    rs_api = CouponsAPI().create_a_coupon(data)

    context.coupon_data = rs_api

@given('I create a coupon with given parameters')
def create_coupons_by_parameters(context):
    parameters = context.text

    data = json.loads(parameters)

    if 'code' not in data:
        data['code'] = generate_random_coupon_code()

    rs_api = CouponsAPI().create_a_coupon(data)
    
    context.coupon_data = rs_api
    context.discount_type = data.get("discount_type", "fixed_cart")


@then("the coupon should existe in database")
@then('Verify the given coupon metadata are recorded correctly')
def verify_the_coupon_data_on_database(context):
    coupons_DAO = CouponsDAO()

    try:
        coupon_data = context.coupon_data
    except AttributeError as e:
        logger.error(f"Error: {e}")
        raise AssertionError(
            "No se ha entregado la data correspondiente al coupon, verificar contexto"
        )

    coupon_id = coupon_data.get("id")


    # Validacion de respuesta de DAO
    rs_coupon_db = coupons_DAO.get_coupon_by_id(coupon_id)
    assert rs_coupon_db, f"El cupón con id {coupon_id} no existe en la base de datos"
    assert (
        len(rs_coupon_db) == 1
    ), f"Se encontraron múltiples registros para el cupón con id {coupon_id}"

    # Validacion de código
    coupon_data_db = rs_coupon_db[0]
    assert coupon_data_db.get("post_title") == coupon_data.get("code"), (
        "El código del cupón no coincide. "
        f'coupon_id: {coupon_id}'
        f'Esperado: {coupon_data.get("code")}, '
        f'Obtenido: {coupon_data_db.get("post_title")}'
    )

    # validacion de estado
    assert coupon_data_db.get("post_status") == "publish", (
        "El estado del cupón no coincide. "
        f'coupon_id: {coupon_id}'
        f'Esperado: publish, '
        f'Obtenido: {coupon_data_db.get("post_status")}'
    )

    coupon_metadata = coupons_DAO.get_coupon_metadata_by_id(coupon_id)

    assert coupon_metadata, (
        f"No se encontraron metadatos para el cupón con id {coupon_id}"
    )

    # Validacion del tipo de descuento
    assert coupon_metadata.get("discount_type") == context.discount_type, (
        "El tipo de descuento no coincide. "
        f'coupon_id: {coupon_id}'
        f'Esperado: {context.discount_type}, '
        f'Obtenido: {coupon_metadata.get("discount_type")}'
    )
