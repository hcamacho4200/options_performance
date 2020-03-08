import datetime

from .instrument import Instrument
from .types import (
    AssetType,
    Instruction
)


class EquityInstrument(Instrument):
    """
    Handle the Option Instrument

    """

    def __init__(self, symbol: str, qty: float, cost: float, instruction: Instruction):
        Instrument.__init__(self, symbol, qty, cost, instruction)
        self._type = AssetType.EQUITY

    @property
    def expiration(self):
        return None

    def profit_loss(self, price: float, date: datetime):
            return price - self.cost
