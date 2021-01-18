# Jessica Chen
# 11/24/2020
# BMW Lab


import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import datetime


url = "http://127.0.0.1:5000/v1/resources/query/"

payload="{\n    \"Collection\": \"IB\"," \
        "\n    \"StartTime\": \"2020-10-01 00:00:00\"," \
        "\n    \"EndTime\": \"2020-10-31 00:00:00\"\n}"

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
    df = df.resample('60min').sum()
    print(df)

    description = df.describe().transpose()
    print(description)

    plot_cols = ['Refilling', 'Heating', 'Cooling',
                 'HotTemp', 'TDS', 'WaterLevel', 'ColdTemp', 'WarmTemp', 'Usage_CC']
    plot_features = df[plot_cols]
    plot_features.index = df.index
    _ = plot_features.plot(subplots=True)
    plt.show()

