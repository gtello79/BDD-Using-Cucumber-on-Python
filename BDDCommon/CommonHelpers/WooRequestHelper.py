from woocommerce import API
from BDDCommon.CommonHelpers.CredentialsHelpers import CredentialsHelpers

base_url = "http://localhost:10009"


class WooRequestHelper:
    def __init__(self) -> None:
        woocommerce_credentials = CredentialsHelpers.get_wc_api_keys()

        consumer_key = woocommerce_credentials["consumer_key"]
        consumer_secret = woocommerce_credentials["consumer_secret"]

        self.wcapi = API(
            url=base_url,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            version="wc/v3",
        )

    def assert_status_code(self):
        assert self.sts_code == self.expected_sts_code, (
            "Status code different. ",
            f"Obtained: {self.sts_code} Expected: {self.expected_sts_code}",
            f"Message: {self.rs.json()}",
        )

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        self.rs = self.wcapi.get(wc_endpoint, params=params)
        self.expected_sts_code = expected_status_code
        self.wc_endpoint = wc_endpoint
        self.sts_code = self.rs.status_code

        self.assert_status_code()

        return self.rs.json()

    def post(self, wc_endpoint, params=None, expected_status_code=200):
        self.rs = self.wcapi.post(wc_endpoint, data=params)
        self.expected_sts_code = expected_status_code
        self.wc_endpoint = wc_endpoint

        self.sts_code = self.rs.status_code
        self.assert_status_code()

        return self.rs.json()

    def delete(self, wc_endpoint, params=None, expected_status_code=200):
        self.rs = self.wcapi.delete(wc_endpoint, params=params)
        self.expected_sts_code = expected_status_code
        self.wc_endpoint = wc_endpoint

        self.sts_code = self.rs.status_code
        self.assert_status_code()

        return self.rs.json()

    def put(self, wc_endpoint, params=None, expected_status_code=200):
        self.rs = self.wcapi.put(wc_endpoint, params=params)
        self.expected_sts_code = expected_status_code
        self.wc_endpoint = wc_endpoint

        self.sts_code = self.rs.status_code
        self.assert_status_code()

        return self.rs.json()


if __name__ == "__main__":
    import random as rd

    print("WooCommerce Library")
    myObj = WooRequestHelper()
    # Example to list products
    # myObj.get("products")

    num = rd.randint(1, 100)

    # Example to add a customer
    email = f"tello_{num}_@example.com"
    password = f"password_{num}_"
    payload = {"email": email, "password": password}

    myObj.post("customers", params=payload, expected_status_code=201)

    print(f"Credential: EMAIL: {email} PASSWORD: {password}")
