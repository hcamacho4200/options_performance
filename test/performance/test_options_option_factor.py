
import performance as p

from performance.options import (
    _handle_option_symbol
)


def test_options_option_factor_single(option_single_long_open):
    """
    Test the single ended option

    :return:
    """
    _option_type = option_single_long_open['transactionItem']['instrument']['putCall']
    _option_symbol = _handle_option_symbol(option_single_long_open['transactionItem']['instrument']['symbol'])
    _option_cost = option_single_long_open['transactionItem']['cost']
    _option_qty = option_single_long_open['transactionItem']['amount']
    _option_effect = option_single_long_open['transactionItem']['positionEffect']

    option_goog_long_call = p.Option(_option_symbol['underlyingSymbol'], _option_type, _option_symbol['strike'],
                                     _option_symbol['optionExpirationDate'], _option_cost, _option_qty, _option_effect)

    options = p.OptionFactory([option_goog_long_call])

    # todo:
    # assert options.risk == 619
