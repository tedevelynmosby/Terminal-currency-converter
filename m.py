import requests
import json
import sys

url = "https://api.ratesapi.io/api/latest"

querystring = {"base":"AUD"}

headers = {
    'Authorization': "Basic Og==",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "5a572626-e43b-4b65-9c61-933a6ef5ec59,31503acb-0844-44c3-9032-07cd3af9d757",
    'Host': "api.ratesapi.io",
    'Cookie': "__cfduid=d61a954e1902fdfe687f83565526959971566986551",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
jsonresp = json.loads(response.text)
arguements = sys.argv[1]
print(jsonresp["rates"]["INR"] * float(arguements))
