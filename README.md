Options Performance
===================

Disclosure: This project is very much a work in progress, at this point no code is remotely production ready


## Vision
To provide a way of processing options trading data so a number of key factors reported:
* Evaluate option campaign performance (adjustment after adjustment)
* Evaluate annualized returns

## Features
* Starting with TD Ameritrade Format and Authentication

## Import Process
* init database tracking
* determine last transaction imported
* append activity
* group by underlying

## Report
* Summary
    * SMIC performance based on start of equity and current value
    * S&P500 Performance
    * MSFT Performance
    * SMIC Performance to Bench Mark
* Running Status
    * starting capital (beginning of year or start of trading)
    * Date of update (API)
    * Days since last change (CALC)
    * New Capital (API)
    * Total Capital (CALC)
    * Current Buying Power (Verticals is the spread, else the margin requirement)
    * Reserves (CALC)
    * Total Sweep (CALC)
    * Equity Positions (CALC)
    * Account Value (Sweep + Equity)
    * SMIC Performance (CALC) starting capital vs acct value
* Position Summary
    * symbol
    * date open
    * total risk
    * total credit
    * annualized profit/loss
        * transaction (type, strike, qty, price) running risk, running credit
* Open Position Summary
* Closed Positions Summary
* Closed Position Performance

## Example Report
* Summary

performance

| SMIC  | S&P 500 | MSFT |
| :---: | :---: | :---: |
| 21% | 31% | 45% |

running stats

|date|days|total<BR>capital|New<BR>Capital|Buying<BR>Power|
|:---:|:---:|:---:|:---:|:---:|
|2020-01-03|2|100000|0|80000|
|2020-01-01|0|100000|0|75000|

position summary

|symbol|open<br>date|close<br>date|days in <br> trade|total<BR>cost|total<BR>risk|ARR|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| NFLX| 2020-01-05 | | | -200 | 1000 | 243 | 


## Setup
create Python Virtual Environment
```
$ python3.7 -m venv options_performance_venv
```
activate Python environment
```
$ . ./options_performance_venv/bin/activate
```
prepare upgrade pip
```
$ pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/00/b6/9cfa56b4081ad13874b0c6f96af8ce16cfbc1cb06bedf8e9164ce5551ec1/pip-19.3.1-py2.py3-none-any.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 8.0MB/s 
Installing collected packages: pip
  Found existing installation: pip 19.0.3
    Uninstalling pip-19.0.3:
      Successfully uninstalled pip-19.0.3
Successfully installed pip-19.3.1
```
install packages
```
$ pip install -r requirements.txt 
Collecting attrs==19.3.0 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/a2/db/4313ab3be961f7a763066401fb77f7748373b6094076ae2bda2806988af6/attrs-19.3.0-py2.py3-none-any.whl
Collecting certifi==2019.11.28 (from -r requirements.txt (line 2))

<snip>

Installing collected packages: attrs, certifi, chardet, idna, more-itertools, zipp, importlib-metadata, six, mock, pyparsing, packaging, pluggy, py, wcwidth, pytest, urllib3, requests
Successfully installed attrs-19.3.0 certifi-2019.11.28 chardet-3.0.4 idna-2.8 importlib-metadata-1.3.0 mock-3.0.5 more-itertools-8.0.2 packaging-19.2 pluggy-0.13.1 py-1.8.0 pyparsing-2.4.5 pytest-5.3.2 requests-2.22.0 six-1.13.0 urllib3-1.25.7 wcwidth-0.1.7 zipp-0.6.0
```
execute tests
```
(options_performance_venv)
$ pytest test/
```
```bash
========================================================================================================================================= test session starts =========================================================================================================================================
platform darwin -- Python 3.7.3, pytest-5.3.2, py-1.8.0, pluggy-0.13.1
rootdir: /Users/hcamacho/hcamacho4200/options_performance
collected 1 item                                                                                                                                                                                                                                                                                      

test/test_process_transactions.py . 
```
