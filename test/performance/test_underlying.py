import datetime

import performance as p


def test_underlying_init():
    """

    :return:
    """

    # test init
    actual = p.Underlying('MSFT')
    assert actual.underlying == 'MSFT'


def test_underlying_transactions():
    """
    Test some transactions

    :return:
    """

    # init the underlying
    actual = p.Underlying('DLTR')

    instruments = [
        p.Instrument(p.AssetType.OPTION, 'DLTR_101819C130', 1, 500.0, p.Instruction.OPENING),
        p.Instrument(p.AssetType.OPTION, 'DLTR_101819C115', -1, -700.0, p.Instruction.OPENING)
    ]

    actual.add_transaction(datetime.datetime.now, instruments)
    assert actual.total_profit == 200.0
