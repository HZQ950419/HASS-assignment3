import json
import numpy as np
import pandas as pd

source_path= 'resale-flat-prices/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv'
year = 2022
month = 3
save_path = 'resale_price_data_{}_{}.json'.format(year, month)

def reader(path):
    pd_reader = pd.read_csv(path)
    prices = {}
    price_list = []
    for i in range(len(pd_reader["month"])):
        if pd_reader["month"][i] == "2022-03":
            if pd_reader["town"][i] not in prices:
                prices[pd_reader["town"][i]] = [pd_reader["resale_price"][i]/pd_reader["floor_area_sqm"][i]]
            else:
                prices[pd_reader["town"][i]].append(pd_reader["resale_price"][i]/pd_reader["floor_area_sqm"][i])
    for elem in prices:
        prices[elem] = np.mean(prices[elem])
        price_list.append(prices[elem])
    print(len(price_list))
    print(min(price_list))
    print(sorted(price_list))
    return prices

prices = reader(source_path)
with open(save_path, 'w') as f:
    json.dump(prices, f)