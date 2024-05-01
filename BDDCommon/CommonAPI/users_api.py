from BDDCommon.CommonHelpers.WooRequestHelper import WooRequestHelper


class CustomerAPI:
    def __init__(self) -> None:
        self.request_helpers = WooRequestHelper()

    def create_user(self, data: dict = {}):
        rs_woocommerce = self.request_helpers.post(
            "customers", data, expected_status_code=201
        )

        return rs_woocommerce