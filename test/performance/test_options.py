# import pytest
#
# import performance as p
#
# from performance.options import (
#     _handle_option_effect,
#     _handle_option_expiration,
#     _handle_option_type,
#     _handle_option_symbol
# )
#
#
#
#
# def test_option_handle_option_symbol():
#     """
#     Test the handling of the symbol
#     - handle a .0 strike
#     - handle a .5 strike
#     :return:
#     """
#     _symbol = 'GOOG_122019C1360'
#
#     actual = _handle_option_symbol(_symbol)
#     assert actual['underlyingSymbol'] == 'GOOG'
#     assert actual['optionExpirationDate'] == '122019'
#     assert actual['optionType'] == 'C'
#     assert float(actual['strike']) == 1360.0
#
#     _symbol = 'GOOG_122019C1360.5'
#
#     actual = _handle_option_symbol(_symbol)
#     assert actual['underlyingSymbol'] == 'GOOG'
#     assert actual['optionExpirationDate'] == '122019'
#     assert actual['optionType'] == 'C'
#     assert float(actual['strike']) == 1360.5






