import datetime

from enum import Enum
from typing import List

from .types import Instruction
from .instrument import Instrument


class Underlying:
    """
    The underlying is a collection of transactions for a specific asset including equity and options manuvers during a
    contigous time. Because options expire, exercise, adjust and a part of options trading does include being assigned
    any manuvers for an underlying are tracked. Once a position goes flat (100% out of the market) for two days tracking
    for the underlying is stopped and performance is entered into the ledger.

    Initialization: The system will initiate the following:
    - position start date
    - underlying assset

    There are two states: Open or Closed.

    Open: While the position is open the system will:
    - allow the adding of transactions
    - update total risk
    - total capital
    - projected return on capital

    Closed: The system will finalize a number of items including:
    - Total use of capital.
    - Total days that capital was used.
    - Total PL during the time.
    - position end date.

    attributes:
        _instruments: dict a dict of instruments used while tracking performance
        _underlying: str
        _start_date: datetime
        _end_date: datetime
        _transactions: list of transactions


    """

    def __init__(self, underlying: str):
        """
        Create the new structure to track an underlying

        :param underlying:
        """
        self._instruments = {}
        self._underlying = underlying
        self._start_date = None
        self._end_date = None

        self._total_credit = float(0)
        self._total_debit = float(0)

    def _update_profit(self, cost: float):
        """
        Update the profit counters
        - if >0 then increase debit
        - if <0 then increase credit

        :param cost:
        :return:
        """

        if cost > 0:
            self._total_debit += cost
        else:
            self._total_credit += -(cost)

    def add_transaction(self, date: datetime, instruments: List[Instrument]):
        """
        Add a transaction to the log for this underlying. Either an opening or closing transaction, and based on this may
        require capital use values.

        :param date: date of the transaction, if this is the 1st transaction when we start coverage of the underlying on this date
        :param instruction: opening or closing
        :param instruments: List[Instrument]

        Must track/calculate the following:

        :param credit: total credit a positive number
        :param debit: total debit a positive number
        :param expiration: if the asset expires track the date
        :param capital_use: capital in use
        :return:
        """

        for inst in instruments: # type: Instrument
            self._update_profit(inst.cost)

    @property
    def total_profit(self):
        return self._total_credit - self._total_debit

    @property
    def total_credit(self):
        return self._total_credit

    @property
    def total_debit(self):
        return self._total_debit

    @property
    def underlying(self) -> str:
        return self._underlying

    @property
    def start_date(self) -> datetime.datetime:
        return self._start_date

