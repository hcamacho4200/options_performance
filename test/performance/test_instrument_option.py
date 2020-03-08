import datetime
import pytest

import performance as p

from performance.instrument_option import (
    _handle_option_expiration,
    _handle_option_symbol,
    _handle_option_type
)


def test_option_handle_option_expiration():
    """
    Test to handle option expiration

    :return:
    """

    actual = _handle_option_expiration('122019')
    assert actual


def test_option_handle_option_type():
    """
    Check to make sure handle option type properly works

    :return:
    """

    assert _handle_option_type('C') == p.OptionType.CALL
    assert _handle_option_type('c') == p.OptionType.CALL
    assert _handle_option_type('P') == p.OptionType.PUT
    assert _handle_option_type('p') == p.OptionType.PUT
    with pytest.raises(p.OptionError):
        _handle_option_type('z')

    assert _handle_option_type('CALL') == p.OptionType.CALL
    assert _handle_option_type('Call') == p.OptionType.CALL
    assert _handle_option_type('call') == p.OptionType.CALL
    assert _handle_option_type('PUT') == p.OptionType.PUT
    assert _handle_option_type('Put') == p.OptionType.PUT
    assert _handle_option_type('put') == p.OptionType.PUT
    with pytest.raises(p.OptionError):
        _handle_option_type('calls')
    with pytest.raises(p.OptionError):
        _handle_option_type('puts')


def test_option_instrument_handle_option_symbol():
    """
    Test the handling of the symbol
    - handle a .0 strike
    - handle a .5 strike
    :return:
    """
    _symbol = 'GOOG_122019C1360'

    actual = _handle_option_symbol(_symbol)
    assert actual['underlyingSymbol'] == 'GOOG'
    assert actual['optionExpirationDate'] == '122019'
    assert actual['optionType'] == 'C'
    assert float(actual['strike']) == 1360.0

    _symbol = 'GOOG_122019C1360.5'

    actual = _handle_option_symbol(_symbol)
    assert actual['underlyingSymbol'] == 'GOOG'
    assert actual['optionExpirationDate'] == '122019'
    assert actual['optionType'] == 'C'
    assert float(actual['strike']) == 1360.5


def test_option_instrument():
    """

    :return:
    """

    # long call full loss
    actual = p.OptionInstrument('DLTR_101819C130', 1, 5.0, p.Instruction.OPENING)
    assert actual.symbol == 'DLTR_101819C130'
    assert actual.qty == 1
    assert actual.price == 5.0
    assert actual.expiration == datetime.datetime.strptime('101819', '%m%d%y')
    assert actual.profit_loss(140, actual.expiration + datetime.timedelta(days=1)) == -500
    assert actual.profit_loss(140, actual.expiration) == -500 + 140

    # short call full loss
    actual = p.OptionInstrument('DLTR_101819C130', -1, 5.0, p.Instruction.OPENING)
    assert actual.profit_loss(140, actual.expiration + datetime.timedelta(days=1)) == 500


    # assert actual.profit_loss(140, actual.expiration) == 1000-500
    #
    # assert actual.is_equity == False
    # assert actual.is_option == True