import base64
import json

import requests

from config.settings.base import PAYMENTS_KEY


class TossPayment():
    @staticmethod
    def success(cls, id, orderId, amount, paymentKey):

        url = "https://api.tosspayments.com/v1/payments/confirm"

        userpass = PAYMENTS_KEY + ':'
        encoded_u = base64.b64encode(userpass.encode()).decode()

        headers = {
            "Authorization": "Basic %s" % encoded_u,
            "Content-Type": "application/json"
        }

        params = {
            "orderId": orderId,
            "amount": amount,
            "paymentKey": paymentKey,
        }

        res = requests.post(url, data=json.dumps(params), headers=headers)
        resjson = res.json()
        pretty = json.dumps(resjson, indent=4)
