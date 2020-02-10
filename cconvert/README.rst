# Terminal-currency-converter

This is a rest based service written with python that uses the existing https://api.ratesapi.io service to get the JSON output for all the currencies with respect to a base currency. Usually the base currency can be altered according to the users needs.

A simple get call example can explain the working

```
https://api.ratesapi.io/api/latest?base=USD
```
The above example returns a JSON that contains the corresponding values of the present day currency with respect to the base currency provided in the URL. 


## Installation

Use the package manager [pip](https://pypi.org/project/cconvert/) to install cconvert.

```
pip install cconvert
```

## Usage

```
cconvert 1 usd inr
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)