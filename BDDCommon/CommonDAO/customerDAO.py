from BDDCommon.CommonHelpers.DBHelpers import DBHelpers

class CustomerDAO:
    def __init__(self) -> None:
        self.db_helper = DBHelpers()

    def get_user_by_email(self, email:str):

        if not email:
            raise Exception('No se ha pasado un email para encontrar al usuario')

        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}'"

        # Execution select function
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql