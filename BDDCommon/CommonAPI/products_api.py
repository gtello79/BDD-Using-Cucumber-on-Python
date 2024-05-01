from BDDCommon.CommonHelpers.WooRequestHelper import WooRequestHelper


class ProductsAPI:
    def __init__(self) -> None:
        self.request_helpers = WooRequestHelper()

    def list_all_products(self) -> list:
        
        params = {
            'per_page': 100
        }
        
        products_list = self.request_helpers.get(
            "products", params=params, expected_status_code=200
        )

        return products_list

    def get_a_product_by_id(self, product_id:int) -> dict:

        rs_api = self.request_helpers.get(wc_endpoint=f'products/{product_id}', expected_status_code=200)

        return rs_api