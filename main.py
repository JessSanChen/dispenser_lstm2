# Jessica Chen
# 11/24/2020
# BMW Lab


import pandas as pd
import requests
import json
import datetime


url = "http://127.0.0.1:5000/v1/resources/query/"

payload="{\n    \"Collection\": \"IB\"," \
        "\n    \"Device_ID\": \"IB_03_01\"," \
        "\n    \"StartTime\": \"2020-07-08 00:00:00\"," \
        "\n    \"EndTime\": \"2020-07-09 00:00:00\"\n}"
headers = {
  'Content-Type': 'application/json'
}


def read_data(url, payload, headers):
    response = requests.request("GET", url, headers=headers, data=payload)
    resp_dict = json.loads(response.text)
    resp_array = resp_dict['result']
    data = pd.json_normalize(resp_array)
    return data


if __name__ == '__main__':
    df = read_data(url, payload, headers)
    df = df.set_index(['UploadTime'])
    df.index = pd.to_datetime(df.index)
    df = df.resample('5min').sum()
    print(df)


