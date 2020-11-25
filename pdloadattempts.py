# Jessica Chen
# 11/24/2020
# BMW Lab

# failed attempts, saved for memory


import pandas as pd
import requests
import json


url = "http://127.0.0.1:5000/v1/resources/query/"

payload="{\n    \"Collection\": \"IB\",\n    \"Device_ID\": \"IB_03_01\",\n    \"StartTime\": \"2020-07-08 00:00:00\",\n    \"EndTime\": \"2020-07-08 01:00:00\"\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)


print(response.text)
print(response.headers)
print(type(response))
print(type(response.text))
# dfs = []
# for doc in response.text:
#     resp_json = json.loads(doc)
#     dfs.append(pd.DataFrame([resp_json]))
#
# df = pd.concat(dfs, ignore_index=True, sort=False)
# print(df)


# query = {
#     "Collection": "IB",
#     "Device_ID": "IB_03_01",
#     "StartTime": "2020-07-08 00:00:00",
#     "EndTime": "2020-07-08 01:00:00"
# }
# resp = requests.get("http://127.0.0.1:5000/v1/resources/query/", params=query)
# print(resp)
# print(type(resp))
# resp_dict = json.loads(resp.text)
# print(resp_dict)
# hdrs = resp.headers
# print(hdrs)
# resp_json = resp.json()
# print(resp_json)
# data = resp_json["results"]
# print(data)
# data_str = json.dumps(data)
# print(pd.read_json(resp, orient='list'))
df = pd.read_json(response.text)
print(df)
#
# print(df)


