from BDDCommon.CommonHelpers.DBHelpers import DBHelpers
import random as rd

class ProductsDAO:
    def __init__(self) -> None:
        self.db_helper = DBHelpers()

    def get_app_products_from_db(self, ordered_by: str = "ASC", limit:int = -1) -> list:

        #Refactoring order function
        ordered_by_func = "ASC"
        if ordered_by == "DESC":
            ordered_by_func = "DESC"

        # Defining limit function
        sql = f"SELECT * FROM local.wp_posts WHERE post_type = 'product' ORDER BY id {ordered_by_func}"
        if limit >= 0:
            sql += f' LIMIT {limit}'
        elif limit == -1:
            pass
        else:
            raise Exception('Se ha definido un valor de limit no correcto. Debe ser mayor que 0, o -1 si es que se quieren todos los elementos')

        # Execution select function
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_random_products_from_db(self, ordered_by: str = "ASC", n_products:int = 1) -> list:

        limit = 5000
        products_list = self.get_app_products_from_db(ordered_by, limit)

        selected_products = rd.sample(products_list, n_products)

        return selected_products