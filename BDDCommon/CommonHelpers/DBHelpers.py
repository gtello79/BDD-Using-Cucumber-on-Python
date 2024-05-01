import pymysql
import pymysql.cursors
from BDDCommon.CommonHelpers.CredentialsHelpers import CredentialsHelpers


class DBHelpers:
    def __init__(self) -> None:
        self.socket = "/home/dragon/.config/Local/run/tt82wb0bQ/mysql/mysqld.sock"

        db_credential = CredentialsHelpers.get_db_credentials()
        self.host = "localhost"
        self.db_user = db_credential["db_user"]
        self.db_password = db_credential["db_password"]

    def create_connection(self):

        self.connection = pymysql.connect(
            host=self.host,
            user=self.db_user,
            password=self.db_password,
            unix_socket=self.socket,
            cursorclass=pymysql.cursors.DictCursor,
        )

    def execute_select(self, sql):
        self.create_connection()
        with self.connection.cursor() as cur:
            cur.execute(sql)
            rs_dict = cur.fetchall()

        return rs_dict

    def execute_sql(self):
        pass
