import datetime
import pytest

from performance.instrument import (
    InstrumentError,
    Instrument,
    Instruction
)


def test_instrument():
    """

    :return:
    """

    actual = Instrument('MSFT', 1, 180.0, Instruction.OPENING)
    assert actual.symbol == 'MSFT'
    assert actual.qty == 1

    with pytest.raises(InstrumentError):
        assert actual.expiration == 1

    with pytest.raises(InstrumentError):
        assert actual.profit_loss(100, datetime.datetime.now())
