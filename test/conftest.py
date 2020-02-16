import json
import pytest


@pytest.fixture()
def td_ameritrade_transaction_content():
    f = open('test/data/td-ameritrade-transactions.json')
    return f.read()


@pytest.fixture()
def td_ameridata_transaction_obj(td_ameritrade_transaction_content):
    return json.loads(td_ameritrade_transaction_content)

@pytest.fixture()
def option_single_long_open():
    return {
        "transactionItem": {
            "accountId": 123456789,
            "amount": 1.0,
            "price": 6.19,
            "cost": -619.0,
            "instruction": "BUY",
            "positionEffect": "OPENING",
            "instrument": {
                "symbol": "GOOG_122019C1360",
                "underlyingSymbol": "GOOG",
                "optionExpirationDate": "2019-12-20T06:00:00+0000",
                "putCall": "CALL",
                "cusip": "0GOOG.LK91360000",
                "description": "GOOG Dec 20 2019 1360.0 Call",
                "assetType": "OPTION"
            }
        }
    }

