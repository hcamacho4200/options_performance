import performance as p


def test_instrument():
    """

    :return:
    """

    actual = p.Instrument(p.AssetType.EQUITY, 'MSFT', 1, 180.0, p.Instruction.OPENING)
    assert actual.symbol == 'MSFT'
    assert actual.qty == 1

    actual.add(2)
    assert actual.qty == 3

    actual.add(-4)
    assert actual.qty == -1

    assert actual.is_flat is False

    actual.add(1)
    assert actual.is_flat is True
