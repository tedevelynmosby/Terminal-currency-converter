import requests
import json
import sys
import traceback
import argparse


def main():
    url = "https://api.ratesapi.io/api/latest"
    
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='USAGE : cconvert 1 usd inr'),
    parser.add_argument("VALUE:", help="Value to be converted. Eg : 1",
                        type=str),
    parser.add_argument("BASE:", help="Base currency value. Eg : usd",
                        type=str),
    parser.add_argument("CONVERT:", help="Convert currency value. Eg : inr",
                        type=str)
    args = parser.parse_args()
    
    try:
        #value of the base currency to be converted
        baseCurrency = sys.argv[2].upper()
        #base currency based on which the conversion should happen
        convertCurrency = sys.argv[3].upper()
    except:
        print("Please enter command line arguments to proceed.")
        print(args)
        sys.exit(1)


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
        
if __name__ == '__main__':
    main()