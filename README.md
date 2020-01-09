Options Performance
===================

## Features
- Starting with TD Ameritrade Format and Authentication

## Setup
* create Python Virtual Environment
```
hcamacho-mn2: hcamacho$ python3.7 -m venv options_performance_venv
```
* activate Python environment
```
hcamacho-mn2: hcamacho$ . ./options_performance_venv/bin/activate
```
* prepare upgrade pip
```
hcamacho-mn2: hcamacho$ pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/00/b6/9cfa56b4081ad13874b0c6f96af8ce16cfbc1cb06bedf8e9164ce5551ec1/pip-19.3.1-py2.py3-none-any.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 8.0MB/s 
Installing collected packages: pip
  Found existing installation: pip 19.0.3
    Uninstalling pip-19.0.3:
      Successfully uninstalled pip-19.0.3
Successfully installed pip-19.3.1
```
* install packages
```
hcamacho-mn2: hcamacho$ pip install -r requirements.txt 
Collecting attrs==19.3.0 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/a2/db/4313ab3be961f7a763066401fb77f7748373b6094076ae2bda2806988af6/attrs-19.3.0-py2.py3-none-any.whl
Collecting certifi==2019.11.28 (from -r requirements.txt (line 2))

<snip>

Installing collected packages: attrs, certifi, chardet, idna, more-itertools, zipp, importlib-metadata, six, mock, pyparsing, packaging, pluggy, py, wcwidth, pytest, urllib3, requests
Successfully installed attrs-19.3.0 certifi-2019.11.28 chardet-3.0.4 idna-2.8 importlib-metadata-1.3.0 mock-3.0.5 more-itertools-8.0.2 packaging-19.2 pluggy-0.13.1 py-1.8.0 pyparsing-2.4.5 pytest-5.3.2 requests-2.22.0 six-1.13.0 urllib3-1.25.7 wcwidth-0.1.7 zipp-0.6.0
```
* execute tests
```
(options_performance_venv) [~/hcamacho4200/options_performance] (master)
hcamacho-mn2: hcamacho$ pytest test/
```
```bash
========================================================================================================================================= test session starts =========================================================================================================================================
platform darwin -- Python 3.7.3, pytest-5.3.2, py-1.8.0, pluggy-0.13.1
rootdir: /Users/hcamacho/hcamacho4200/options_performance
collected 1 item                                                                                                                                                                                                                                                                                      

test/test_process_transactions.py . 
```
