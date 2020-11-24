# Jessica Chen
# 11/24/2020
# BMW Lab


import pandas as pd
import requests

query = {
    "Collection": "IB",
    "Device_ID": "IB_03_01",
    "StartTime": "2020-07-08 00:00:00",
    "EndTime": "2020-07-08 01:00:00"
}
resp = requests.get("http://127.0.0.1:5000/v1/resources/query/", params=query)
df = pd.read_json(resp)

print(df)
