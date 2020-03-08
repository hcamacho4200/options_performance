import datetime
import pytest

import performance as p


def test_equity_instrument():
    """

    :return:
    """

    actual = p.EquityInstrument('MSFT', 1, 180.0, p.Instruction.OPENING)
    assert actual.symbol == 'MSFT'
    assert actual.qty == 1
    assert actual.expiration is None
    assert actual.profit_loss(100, datetime.datetime.now()) == -80
    assert actual.is_equity == True
    assert actual.is_option == False