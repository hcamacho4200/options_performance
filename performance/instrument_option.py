import datetime
import re

from enum import Enum

from .instrument import Instrument
from .types import (
    AssetType,
    Instruction
)


_p_option_symbol = re.compile(r'(.*)_(\d{6})(.)(.*)')

_GOOD_DATE_FORMATS = [
    ('%m%d%y', '04012019')
    # ('%Y-%m-%d %H:%M', '2019-04-01 13:00'),
    # ('%Y-%m-%d', '2019-04-01'),
    # ('%Y/%m/%d %H:%M', '2019/04/01 13:00'),
    # ('%Y/%m/%d', '2019-04-01'),
    # ('%m%d%y%H%M', '0401191300')
]


class OptionError(Exception):
    """
    Raise when there is a problem with the option class
    """
    pass


class OptionType(Enum):
    CALL = 1
    PUT = 2


def _handle_option_expiration(date_string: str) -> datetime:
    """
    Convert a date string into a datetime using formats defined in GOOD_DATE_FORMATS
    - once converted add 1 day, the expiration for value is the following day


    :param date_string: date string to test
    :return: datetime
    """

    for format, example in _GOOD_DATE_FORMATS:
        try:
            return datetime.datetime.strptime(date_string, format)
        except ValueError:
            pass

    return None


def _handle_option_type(option_type: str):
    """
    Handle setting the option type, supported types (PUT/CALL)
    - 'C'
    - 'CALL'
    - 'P'
    - "PUT'

    Handle the above case insensitive.

    :param option_type:
    :return: OptionType
    """
    _raise = False
    _type = None

    if len(option_type) == 1:
        if option_type.lower() == 'c':
            _type = OptionType.CALL
        elif option_type.lower() == 'p':
            _type = OptionType.PUT
        else:
            _raise = True
    else:
        if option_type.lower() == 'call':
            _type = OptionType.CALL
        elif option_type.lower() == 'put':
            _type = OptionType.PUT
        else:
            _raise = True

    if _raise:
        raise OptionError('_handle_option_type does not support {}'.format(option_type))

    return _type


def _handle_option_symbol(option_symbol: str):
    """
    Handle an option symbol, return the following:
    - underlying symbol
    - expiration
    - option_type
    - strike_price

    :param option_symbol:
    :return:
    """

    match = _p_option_symbol.match(option_symbol)
    if (match):
        return {
            'underlyingSymbol': match.group(1),
            'optionExpirationDate': match.group(2),
            'optionType': match.group(3),
            'strike': match.group(4)
        }



class OptionInstrument(Instrument):
    """
    Handle the Option Instrument

    """

    def __init__(self, symbol: str, qty: float, cost: float, instruction: Instruction, contract_size: int = 100):
        """

        :param symbol:
        :param qty:
        :param cost:
        :param instruction:
        :param contract_size: the number of underlying per contract (100 by default)

        """
        Instrument.__init__(self, symbol, qty, cost, instruction)

        self._type = AssetType.OPTION
        self._contract_size = contract_size

        option_data = _handle_option_symbol(symbol)
        self._option_underlying = option_data['underlyingSymbol']
        self._option_type = _handle_option_type(option_data['optionType'])
        self._option_strike = float(option_data['strike'])
        self._option_expiration = _handle_option_expiration(option_data['optionExpirationDate'])

    @property
    def contract_size(self):
        return self._contract_size

    @property
    def expiration(self):
        return self._option_expiration

    def profit_loss(self, price: float, date: datetime):
        """
        Compute the profit/loss based on the price and the date
        - if expired, then return 0 (maybe wrong)
        - compute the absolte value of profit based on strike and price
        - determine sign of profits based on option type

        :param price:
        :param date:
        :return:
        """

        if date > self.expiration:
            if self.qty > 0:
                return -self.cost
            if self.qty < 0:
                return self.cost
            else:
                return 0


        # table
        # qty   type    strike  premium     price
        # 1     C       130     500         140     price - strike
        #                                            10 * 100 = 1000 - 500 = 500

        _abs_pl = (abs(price - self.option_strike)) * self.option_contract_size

        if price > self.option_strike:
            if self._option_type == OptionType.CALL:
                if self.qty >= 0:
                    pass
                else:
                    _abs_pl = -1 * _abs_pl

        return price - self.cost

    @property
    def option_contract_size(self) -> int:
        return self._contract_size

    @property
    def option_strike(self) -> float:
        return self._option_strike

