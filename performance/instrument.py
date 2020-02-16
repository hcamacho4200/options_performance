from .types import (
    AssetType,
    Instruction
)


class Instrument:
    """
    Define the instrument for a transaction

    Attributes:
        _type: AssetType
        _symbol: str
        _qty: float
        _cost: flat
        _instruction: Instruction

    """

    def __init__(self, type: AssetType, symbol: str, qty: float, cost: float, instruction: Instruction):
        """

        :param type: Equity, option, etc
        :param symbol: stock ticker or CUSIP
        :param qty:
        :param cost: total cost of the instrument, >0 is a debit, <= is a credit
        :param instruction: open or close

        """

        self._symbol = symbol
        self._qty = qty
        self._cost = cost
        self._instruction = instruction

    def add(self, float):
        self._qty += float

    @property
    def is_flat(self) -> bool:
        if self._qty == 0:
            return True
        else:
            return False

    @property
    def cost(self):
        return self._cost

    @property
    def instruction(self) -> Instruction:
        return self._instruction

    @property
    def qty(self) -> float:
        return self._qty

    @property
    def symbol(self) -> str:
        return self._symbol

