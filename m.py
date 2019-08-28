import requests
import json
import sys

url = "https://free.currconv.com/api/v7/convert"

querystring = {"q":"USD_INR","compact":"ultra","apiKey":"290c9c851dc7c10c7e40"}

headers = {
    'Authorization': "Basic Og==",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "ccd70a1f-c0d4-4b80-8343-26accd1199a0,69d5a5d6-9e40-47af-bf4b-d6351c064bde",
    'Host': "free.currconv.com",
    'Cookie': "__cfduid=da34e8e562f237f9222a02b5c0f14affb1565585170",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
arguements = sys.argv[1]
jresp = json.loads(response.text)
print(jresp["USD_INR"] * float(arguements))
