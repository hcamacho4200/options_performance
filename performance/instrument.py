import datetime

from .types import (
    AssetType,
    Instruction
)


class InstrumentError(Exception):
    """ raise exception when there is a problem with the baseclass"""
    pass


class Instrument:
    """
    Define the instrument for a transaction

    Baseclass will collect symbol, cost, qty, and instruction

    Subclasses are expected to implement properties:
    - expiration
    - value (asset price, date)

    Attributes:
        _type: AssetType
        _symbol: str
        _qty: float
        _cost: flat
        _instruction: Instruction
        _expiration: DateTime

    """

    def __init__(self, symbol: str, qty: float, price: float, instruction: Instruction):
        """

        :param symbol: stock ticker or CUSIP
        :param qty:
        :param price:
        :param instruction: open or close

        """

        self._type = None
        self._symbol = symbol
        self._qty = qty
        self._price = price
        self._instruction = instruction

    @property
    def price(self):
        return self._price

    @property
    def cost(self):
        """
        Derived from qty * price to get cost.
        :return:
        """
        return self.qty * self.price

    @property
    def instruction(self) -> Instruction:
        return self._instruction

    @property
    def is_equity(self) -> bool:
        return True if self._type == AssetType.EQUITY else False

    @property
    def is_option(self) -> bool:
        return True if self._type == AssetType.OPTION else False

    @property
    def qty(self) -> float:
        return self._qty

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def expiration(self) -> datetime:
        raise InstrumentError("Property expiration must be overriden by subclass {}".format(type(self)))

    def profit_loss(self, price: float, date: datetime):
        raise InstrumentError("value method must be overriden by subclass {}".format(type(self)))


