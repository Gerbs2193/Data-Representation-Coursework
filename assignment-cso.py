import json
import requests
# importing necessary module and library needed for brief

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"
response = requests.get(url)
# cso url json and the get request needed to retrieve the data from the web


data = response.json()
with open("cso.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
# indent 4 mformats the json in a neat way. 
print("All worked and is stored in 'cso.json'.")