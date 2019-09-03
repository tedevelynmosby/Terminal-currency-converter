# Terminal-currency-converter

This is a rest based service written with python that uses the existing https://api.ratesapi.io service to get the JSON output for all the currencies with respect to a base currency. Usually the base currency can be altered according to the users needs.

A simple get call example can explain the working

```
https://api.ratesapi.io/api/latest?base=USD
```
The above example returns a JSON that contains the corresponding values of the present day currency with respect to the base currency provided in the URL. 

## Getting Started
The python file *p.my* provides the wrappers for terminal level access.

The input parameters are : 
```
python m.py valueOfCurrency BaseCurrency ResultantCurrency
```
Example:

```
python m.py 20 usd inr
```

```
python m.py 19 AUD EUR
```
## Installation

Brew setup is yet to be integerated.
