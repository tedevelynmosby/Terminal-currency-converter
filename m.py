import requests
import json
import sys

url = "https://api.ratesapi.io/api/latest"

#value of the base currency to be converted
baseCurrency = sys.argv[2].upper()

#base currency based on which the conversion should happen
convertCurrency = sys.argv[3].upper()


querystring = {"base":baseCurrency.upper()}

headers = {'Host': "api.ratesapi.io"}

response = requests.request("GET", url, headers=headers, params=querystring)
jsonresp = json.loads(response.text)

#Resultant currency that needs to be converted to
arguements = sys.argv[1]

#Multiply the resultant currency value with the base to display the current value
print(jsonresp["rates"][convertCurrency] * float(arguements))
