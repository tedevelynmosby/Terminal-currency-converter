import requests
import json
import sys
import traceback

url = "https://api.ratesapi.io/api/latest"

#value of the base currency to be converted
baseCurrency = sys.argv[2].upper()

#base currency based on which the conversion should happen
convertCurrency = sys.argv[3].upper()


querystring = {"base":baseCurrency.upper()}

headers = {'Host': "api.ratesapi.io"}

response = requests.request("GET", url, headers=headers, params=querystring)
try:
    #Raise exception if url is status code is not 200.
    response.raise_for_status()
    jsonresp = json.loads(response.text)
    #Resultant currency that needs to be converted to
    arguements = sys.argv[1]
    #Multiply the resultant currency value with the base to display the current value
    convertedResponse = '{:.2f}'.format(jsonresp["rates"][convertCurrency] * float(arguements))
    print(str(sys.argv[1] + " " + str(baseCurrency) + " to " + str(convertCurrency) +  " => " + str(convertedResponse)) + " " + str(convertCurrency).lower())
    
except:
    print("\n===================\n BRUHception occured. You got BRUHed by the service or the currency you entered! Please check the stacktrace king. \n==================\n")
    traceback.print_exc()
    sys.exit(1)
