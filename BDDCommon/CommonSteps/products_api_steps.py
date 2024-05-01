from behave import step, then
from BDDCommon.CommonDAO.orderDAO import OrderDAO
from BDDCommon.CommonDAO.productsDAO import ProductsDAO
from BDDCommon.CommonAPI.products_api import ProductsAPI
from BDDCommon.CommonConfigs.locatosconfig import (
    NAV_BAR_LOCATORS,
    ORDER_RECEIVED_LOCATORS,
)
from BDDCommon.CommonFuncs.webcommon import WebCommon


@step("I get number of available products from {source}")
def get_number_of_products_from_source(context, source):
    if source == "db":
        # get all available products with SQL
        all_rows = ProductsDAO().get_app_products_from_db()

        # then set the number available product as context variable
        context.qty_products_db = len(all_rows)

    if source == "api":
        products_api = ProductsAPI()
        products_len = len(products_api.list_all_products())

        context.qty_products_api = products_len


@step("I get {n_products} random product from database")
def get_random_product_from_database(context, n_products: int):
    products_dao = ProductsDAO()

    try:
        n_products = int(n_products)
    except TypeError as e:
        raise (
            f"La cantidad de productos debe ser un número entero. ERROR en {n_products}"
        )

    product_list = products_dao.get_random_products_from_db(
        ordered_by="RAND", n_products=n_products
    )

    context.product_list = product_list


@then("I verify order is created in database")
def verify_the_order_on_database(context):
    try:
        order_number = context.order_context['order_number'] 
        int(order_number)
    except AttributeError as e:
        raise AssertionError("No se ha encontrado el número de orden en el contexto")
    except TypeError as e:
        raise AssertionError("El número de orden no es un número válido. ERROR en {order_number}")

    # Consulta por el objeto en bd
    rs_bd = OrderDAO().get_order_by_id(order_number)

    # Validacion de la respuesta obtenida por bd
    assert len(rs_bd) == 1, (
        f"La cantidad de ordenes encontradas con el número {order_number} no es 1"
        f"Obtenido: {len(rs_bd)}"
    )

    order_bd = rs_bd[0]


    assert order_bd['post_type'] == 'shop_order_placehold',( 
        'El tipo de orden no es shop_order. '
        f'Obtenido: {order_bd["shop_order_placehold"]} Ticket Number: {order_number}'
    )

@then("I verify the {field} products in database is the same as in UI")
def verify_products_in_db_and_ui(context, field):
    objective_field = ['order_date', 'order_total']

    if field not in objective_field:
        raise AssertionError(f"El campo {field} no es un campo válido")
    
