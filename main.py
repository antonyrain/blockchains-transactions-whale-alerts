from api_key import api_key
import requests
import time
import pandas as pd

pd.options.display.max_rows = 999
pd.options.display.max_columns = 99

local_date_time = time.localtime()  # get struct_time
time_string = time.strftime("%H:%M:%S", local_date_time)
print(time_string)

timestamp = int(time.time()) - 900  # current Unix timestamp minus time in seconds for retrieving transactions
value = "500000"  # minimum USD value of transactions returned
currency_code = "btc"

transactions = requests.get(
    f'https://api.whale-alert.io/v1/transactions?api_key={api_key}&min_value={value}&start={timestamp}&currency={currency_code}')

data = transactions.json()
df = pd.DataFrame(data['transactions'])

df.to_excel(f"{currency_code}_{time_string}.xlsx")
# df.to_csv(f"{currency_code}_{time_string}.csv")
