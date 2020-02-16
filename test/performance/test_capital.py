import datetime
import pytest

import performance as p


def test_capital_data():
    """
    Test to make sure capital data is working

    :return:
    """

    start_date = datetime.datetime.now()

    # test standard use
    actual = p.CapitalData(start_date, 200)
    actual.end_date = start_date + datetime.timedelta(days=2)
    assert actual.capital == 200
    assert actual.time_in_use() == 172800

    # test expected expiration
    actual = p.CapitalData(start_date, 200)
    assert actual.capital == 200
    assert actual.time_in_use(expected_expiration=start_date + datetime.timedelta(days=2)) == 172800

    # test if raises exception
    with pytest.raises(p.CapitalDataError):
        actual = p.CapitalData(start_date, 200)
        assert actual.capital == 200
        assert actual.time_in_use() == 172800


def test_capital():
    """
    Test capital tracking.
    - add some capital usage.
    - if first capital, add and set flag to not first
    - if not the first, find previous and set end date

    :return:
    """

    start_date = datetime.datetime.now()

    actual = p.Capital()
    actual.add(start_date, 200)
    assert actual._first == False
    assert actual._data[-1]._capital == 200
    assert actual._data[-1]._end_date == None

def test_capital_report():
    """
    Test capital report with one completely closed transaction
    :return:
    """

    start_date = datetime.datetime.now()
    actual = p.Capital()
    actual.add(start_date, 200)
    actual.close(start_date + datetime.timedelta(days=2))

    report = actual.report_capital_use(start_date + datetime.timedelta(days=100))
    assert report[0] == (200, 172800)

def test_capital_report_multi_open():
    """
    Test capital report with multiple closed transactions with one left open
    :return:
    """

    start_date = datetime.datetime.now()
    actual = p.Capital()
    actual.add(start_date, 200)
    actual.add(start_date + datetime.timedelta(days=2), 400)
    actual.add(start_date + datetime.timedelta(days=10), 800)
    report = actual.report_capital_use(start_date + datetime.timedelta(days=100))

    assert report[0] == (200, 172800)
    assert report[1] == (400, 691200)
    assert report[2] == (800, 7776000)



