# import re
#
# from abc import ABC
# from enum import Enum
# from datetime import datetime
# from typing import List
#
# _p_option_symbol = re.compile(r'(.*)_(\d{6})(.)(.*)')
#
# _GOOD_DATE_FORMATS = [
#     ('%m%d%y', '20190401')
#     # ('%Y-%m-%d %H:%M', '2019-04-01 13:00'),
#     # ('%Y-%m-%d', '2019-04-01'),
#     # ('%Y/%m/%d %H:%M', '2019/04/01 13:00'),
#     # ('%Y/%m/%d', '2019-04-01'),
#     # ('%m%d%y%H%M', '0401191300')
#
# ]
#
#
# class OptionError(Exception):
#     """
#     Raise when there is a problem with the option class
#     """
#     pass
#
#
# class OptionType(Enum):
#     CALL = 1
#     PUT = 2
#
#
# class OptionEffect(Enum):
#     OPEN = 1
#     CLOSE = 2
#
# def _handle_option_expiration(date_string: str) -> datetime:
#     """
#     Convert a date string into a datetime using formats defined in GOOD_DATE_FORMATS
#
#
#     :param date_string: date string to test
#     :return: datetime
#     """
#
#     for format, example in _GOOD_DATE_FORMATS:
#         try:
#             return datetime.strptime(date_string, format)
#         except ValueError:
#             pass
#
#     return None
#
#
#
# def _handle_option_type(option_type: str):
#     """
#     Handle setting the option type, supported types (PUT/CALL)
#     - 'C'
#     - 'CALL'
#     - 'P'
#     - "PUT'
#
#     Handle the above case insensitive.
#
#     :param option_type:
#     :return: OptionType
#     """
#     _raise = False
#     _type = None
#
#     if len(option_type) == 1:
#         if option_type.lower() == 'c':
#             _type = OptionType.CALL
#         elif option_type.lower() == 'p':
#             _type = OptionType.PUT
#         else:
#             _raise = True
#     else:
#         if option_type.lower() == 'call':
#             _type = OptionType.CALL
#         elif option_type.lower() == 'put':
#             _type = OptionType.PUT
#         else:
#             _raise = True
#
#     if _raise:
#         raise OptionError('_handle_option_type does not support {}'.format(option_type))
#
#     return _type
#
#
# def _handle_option_symbol(option_symbol: str):
#     """
#     Handle an option symbol, return the following:
#     - underlying symbol
#     - expiration
#     - option_type
#     - strike_price
#
#     :param option_symbol:
#     :return:
#     """
#
#     match = _p_option_symbol.match(option_symbol)
#     if (match):
#         return {
#             'underlyingSymbol': match.group(1),
#             'optionExpirationDate': match.group(2),
#             'optionType': match.group(3),
#             'strike': match.group(4)
#         }
#
#
# def _handle_option_effect(option_effect: str) -> OptionEffect:
#     """
#     Return the correct option effect
#
#     :param option_effect:
#     :return:
#     """
#     _raise = False
#     _return = None
#
#     if option_effect.lower() in ['open', 'opening']:
#         _return = OptionEffect.OPEN
#     elif option_effect.lower() in ['close', 'closing']:
#         _return = OptionEffect.CLOSE
#     else:
#         _raise = True
#
#     if _raise:
#         raise(OptionError('_handle_option_effect does not support {}'.format(option_effect)))
#
#     return _return
#
#
# class Option():
#     """
#     Base class for an options contract
#
#     """
#
#     def __init__(self, option_underlying: str, option_type: str, option_strike: float, option_exp: datetime, option_premium: float,
#                  option_qty: int, option_effect: str ):
#
#         """
#
#         :param option_underlying:
#         :param option_type:
#         :param option_strike:
#         :param option_exp:
#         :param option_premium:
#         :param option_qty:
#         :param option_effect:
#         """
#
#         self._option_underlying = option_underlying
#         self._option_type = _handle_option_type(option_type)
#         self._option_strike = option_strike
#         self._option_exp = _handle_option_expiration(option_exp)
#         self._option_premium = option_premium
#         self._option_qty = option_qty
#         self._option_effect = _handle_option_effect(option_effect)
#
#     @property
#     def option_underlying(self):
#         return self._option_underlying
#
#     @property
#     def option_type(self):
#         return self._option_type
#
#     @property
#     def option_strike(self):
#         return self._option_strike
#
#     @property
#     def option_exp(self):
#         return self._option_exp
#
#     @property
#     def option_premium(self):
#         return self._option_premium
#
#     @property
#     def option_qty(self):
#         return self._option_qty
#
#     @property
#     def option_effect(self):
#         return self._option_effect
#
#
# class OptionFactoryType(Enum):
#     SINGLE = 1
#     VERTICAL = 2
#
#
# class OptionFactory():
#     """
#     Class to build as a factory to build various options structures with the proper type.
#
#     Generally speaking this object is constructed and is not allowed to mutate since trades aren't allows to mutate. The
#     use of additional transactions allow for a change in a symbols perspective.
#
#     Attributes:
#         _total_Risk: float
#         _total_price: float
#         _type: OptionsFactorType
#
#     """
#
#     def __init__(self, options: List[Option]):
#         """
#         Send a list of options, this factory will figure out what they are and create the proper structure.
#
#         :param options:
#         """
#         self._total_capital_used = None
#
#         # check to see if we are working with a single option
#         if len(options) == 1:
#             self._type = OptionFactoryType.SINGLE
#
#         # check for a 2 option combo.
#         elif len(options) == 2:
#             pass
#
#         self._total_capital_used = self._handle_calc_total_capital_used()
#
#     @property
#     def capital_used(self):
#         return self._total_capital_used
#
#     def _handle_calc_total_capital_used(self):
#         """
#         Calculate the total mount of capital used in this trade.
#         - if short options, calculate the minimum margin requirements
#         - if long options, take the total debit as capital in use.
#
#         :return:
#         """
#
#         _total_capital = 0
#
#         if self._type == OptionFactoryType.SINGLE:
#             pass
#
#         return _total_capital
#
#
#
#
#
#
