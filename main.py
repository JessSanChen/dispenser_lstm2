# Jessica Chen
# 11/24/2020
# BMW Lab


import pandas as pd
import requests
import json

query = {
    "Collection": "IB",
    "Device_ID": "IB_03_01",
    "StartTime": "2020-07-08 00:00:00",
    "EndTime": "2020-07-08 01:00:00"
}
resp = requests.get("http://127.0.0.1:5000/v1/resources/query/", params=query)
print(resp)
print(type(resp))
resp_dict = json.loads(resp.text)
print(resp_dict)
# hdrs = resp.headers
# print(hdrs)
# resp_json = resp.json()
# print(resp_json)
# data = resp_json["results"]
# print(data)
# data_str = json.dumps(data)
# print(pd.read_json(resp, orient='list'))
df = pd.DataFrame(resp["results"])
#
# print(df)
