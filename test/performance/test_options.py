import pytest

import performance as p

from performance.options import (
    _handle_option_effect,
    _handle_option_expiration,
    _handle_option_type,
    _handle_option_symbol
)

def test_option_handle_option_effect():
    """

    :return:
    """

    assert _handle_option_effect(('closing')) == p.OptionEffect.CLOSE
    assert _handle_option_effect(('close')) == p.OptionEffect.CLOSE
    assert _handle_option_effect(('open')) == p.OptionEffect.OPEN
    assert _handle_option_effect(('opening')) == p.OptionEffect.OPEN
    with pytest.raises(p.OptionError):
        _handle_option_effect(('openingsdfsdf'))



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

def test_option_handle_option_symbol():
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



def test_option_handle_option_expiration():
    """
    Test to handle option expiration

    :return:
    """

    actual = _handle_option_expiration('122019')
    assert actual


def test_option_single_long_open(option_single_long_open):
    """
    Test to make sure the structure is working properly
    :return:
    """

    _option_type = option_single_long_open['transactionItem']['instrument']['putCall']
    _option_symbol = _handle_option_symbol(option_single_long_open['transactionItem']['instrument']['symbol'])
    _option_cost = option_single_long_open['transactionItem']['cost']
    _option_qty = option_single_long_open['transactionItem']['amount']
    _option_effect = option_single_long_open['transactionItem']['positionEffect']

    actual = p.Option(_option_symbol['underlyingSymbol'], _option_type, _option_symbol['strike'],
                      _option_symbol['optionExpirationDate'], _option_cost, _option_qty, _option_effect)

    assert actual.option_underlying == 'GOOG'
    assert actual.option_type == p.OptionType.CALL
    assert float(actual.option_strike) == float(1360)
    assert actual.option_exp == _handle_option_expiration('122019')
    assert float(actual.option_premium) == float(-619)
    assert float(actual.option_qty) == float(1)
    assert actual.option_effect == p.OptionEffect.OPEN
