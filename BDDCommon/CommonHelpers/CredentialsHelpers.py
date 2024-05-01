import os


class CredentialsHelpers:
    def __init__(self) -> None:
        pass

    @classmethod
    def get_wc_api_keys(cls) -> dict:
        consumer_key = os.getenv("WOO_KEY")
        consumer_secret = os.getenv("WOO_SECRET")

        if not all([consumer_key, consumer_secret]):
            raise Exception(
                "Las credenciales de WooCommerce no estan definidas como variables de entorno"
            )

        kwargs = {"consumer_key": consumer_key, "consumer_secret": consumer_secret}

        return kwargs

    @classmethod
    def get_db_credentials(cls) -> dict:
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')

        if not all([db_user, db_password]):
            raise Exception(
                "Las credenciales de WooCommerce no estan definidas como variables de entorno"
            )

        kwargs = {"db_user": db_user, "db_password": db_password}

        return kwargs