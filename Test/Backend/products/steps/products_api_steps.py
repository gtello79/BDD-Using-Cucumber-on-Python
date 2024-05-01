from behave import step, then
import random
from BDDCommon.CommonAPI.products_api import ProductsAPI
from BDDCommon.CommonSteps.products_api_steps import *


@then("the total products number in api should be same as in db")
def compare_total_products_number(context):
    qty_products_db = context.qty_products_db
    qty_products_api = context.qty_products_api

    assert (
        qty_products_api == qty_products_db
    ), f"Error en los largos {qty_products_api} {qty_products_db}"


@step("I verify the product api returns correct product by id")
def verify_products_id(context):
    # choose a random element
    product_from_db = random.sample(context.product_list, 1)[0]
    product_id = product_from_db["ID"]

    products_api = ProductsAPI()
    product_from_api = products_api.get_a_product_by_id(product_id=product_id)

    assert (
        product_from_db["ID"] == product_from_api["id"]
    ), f'Error en la llamada del producto. Revisar ids API: {product_from_api["id"]}  DB: {product_from_db["ID"]}'

    assert (
        product_from_db["post_title"] == product_from_api["name"]
    ), f'Error en la llamada del producto. Revisar ids API: {product_from_api["name"]}  DB: {product_from_db["post_title"]}'
