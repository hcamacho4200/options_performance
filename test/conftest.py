import json
import pytest


@pytest.fixture()
def td_ameritrade_transaction_content():
    f = open('test/data/td-ameritrade-transactions.json')
    return f.read()


@pytest.fixture()
def td_ameridata_transaction_obj(td_ameritrade_transaction_content):
    return json.loads(td_ameritrade_transaction_content)