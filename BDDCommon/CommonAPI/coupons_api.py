from BDDCommon.CommonHelpers.WooRequestHelper import WooRequestHelper


class CouponsAPI:
    def __init__(self) -> None:
        self.request_helpers = WooRequestHelper()

    def create_a_coupon(self, data: dict) -> dict:
        rs_api = self.request_helpers.post(
            wc_endpoint="coupons", params=data, expected_status_code=201
        )
        return rs_api

    def get_a_coupon_by_id(self, coupon_id: int) -> dict:
        rs_api = self.request_helpers.get(
            wc_endpoint=f"coupons/{coupon_id}", expected_status_code=200
        )

        return rs_api
