from behave import step
from BDDCommon.CommonConfigs.locatosconfig import MY_HOME_LOCATORS
from BDDCommon.CommonFuncs.webcommon import WebCommon
import random as rd


@step("I add {n_products} random item to cart from the {site}")
def add_products_on_cart(context, n_products: int, site):
    # Escojo el sitio desde donde puedo añadir elementos al carro
    if site.lower() in ("homepage", "home"):
        SITE_LOCATORS = MY_HOME_LOCATORS
    else:
        raise Exception(f"No se han configurado los Locators de {site}")

    # Obtengo los locators de acuerdo al sitio en donde me encuentro
    try:
        add_cart_buttons = SITE_LOCATORS["products-list-on-sell"]
    except KeyError:
        raise KeyError("No se han configurado los locators de products-list")

    # Obtengo los locators segun su llave y valor
    add_cart_buttons_type = add_cart_buttons["type"]
    add_cart_buttons_locator = add_cart_buttons["locator"]

    # Obtengo un listado de webElements
    add_cart_buttons_web_element_list = WebCommon.find_elements(
        context=context,
        locator_attribute=add_cart_buttons_type,
        locator_text=add_cart_buttons_locator,
    )

    try:
        n_products = int(n_products)
    except TypeError as e:
        raise TypeError(
            f"No se ha podido aplicar la transformación al valor {n_products}. "
            f'Error {e}'
        )

    # Selecciono un método al azar
    selected_add_cart_button = rd.sample(
        add_cart_buttons_web_element_list, k=n_products
    )
    for web_element in selected_add_cart_button:
        # Hacer click
        WebCommon.click_element(context_or_web_element=web_element)
