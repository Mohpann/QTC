# Connor Hunter
# 10/8/23
# Script to find stocks doing a stock split within a given time frame

import requests
api_key = '&apikey=K4pRVYD8DW8oeaxFButzBj1j7eQfZ4fr'
start_date = "from=2023-10-03"
end_date = 'to=2023-10-08'
response = requests.get("https://financialmodelingprep.com/api/v3/stock_split_calendar?{}&{}&apikey=K4pRVYD8DW8oeaxFButzBj1j7eQfZ4fr".format(start_date, end_date, api_key))

print (response.json())