from BDDCommon.CommonHelpers.DBHelpers import DBHelpers


class OrderDAO:
    def __init__(self) -> None:
        self.db_helper = DBHelpers()

    def get_order_by_id(self, order_id: int | str):
        sql = f"SELECT * FROM local.wp_posts WHERE ID = {order_id}"

        query = self.db_helper.execute_select(sql)
        return query
