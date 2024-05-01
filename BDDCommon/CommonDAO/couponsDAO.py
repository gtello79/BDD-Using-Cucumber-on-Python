from BDDCommon.CommonHelpers.DBHelpers import DBHelpers

class CouponsDAO:
    def __init__(self) -> None:
        self.db_helper = DBHelpers()

    def get_coupon_by_id(self, coupon_id: int | str):
        sql = f"SELECT * FROM local.wp_posts WHERE ID = {coupon_id} and post_type = 'shop_coupon'"

        query = self.db_helper.execute_select(sql)
        return query

    def get_coupon_metadata_by_id(self, coupon_id: int | str) -> dict:
        sql = f"SELECT * FROM local.wp_postmeta WHERE post_id = {coupon_id}"

        query = self.db_helper.execute_select(sql)

        metadata = dict()
        
        for data in query:
            metadata[data.get("meta_key")] = data.get("meta_value")

        return metadata