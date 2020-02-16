import datetime

from typing import List

class CapitalDataError(Exception):
    """ fire when there is a problem with capital data function"""
    pass


class CapitalData:
    def __init__(self, start_date: datetime, capital: float):
        """

        :param start_date:
        :param capital:
        """

        self._start_date = start_date
        self._end_date = None
        self._capital = capital

    @property
    def end_date(self, end_date: datetime):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    @property
    def capital(self) -> float:
        return self._capital

    def time_in_use(self, expected_expiration: datetime = None) -> int:
        """
        Return time in use
        - if expected_expiration is set then use this as end time for an element that does not have an endtime.

        :return:
        """
        if self._end_date:
            return (self._end_date - self._start_date).total_seconds()
        elif expected_expiration:
            return (expected_expiration - self._start_date).total_seconds()
        else:
            raise CapitalDataError("When calling time_in_use, a capital allocation without end_date must have expiration")


class Capital():
    """
    Capital tracking

    We want to track the amount of capital that is in use, and when it starts.
    - if the 1st track, set the date and set the flag for 1st to False
    - if not 1st, close the previous session with an end date, add the new

    """

    def __init__(self):
        self._data = []
        self._first = True

    def add(self, start_date: datetime, capital: float):
        """
        Add a capital use section

        :param start_date:
        :param capital:
        :return:
        """

        if not self.first:
            self.close(start_date)
        else:
            self._first = False

        self._data.append(CapitalData(start_date, capital))

    def close(self, date: datetime):
        """
        Use to close a date section, normally the last date.

        :param date:
        :return:
        """

        self._data[-1].end_date = date

    def report_capital_use(self, expected_expiration: datetime = None) -> list:
        """
        Built a structure that reports the following:
        - amount of capital
        - time in use

        :return:
        """

        return [(_cd._capital, _cd.time_in_use(expected_expiration)) for _cd in self._data] # type: CapitalData


    @property
    def first(self):
        return self._first


