# Connor Hunter
# 10/8/23
# 

import requests
ticker = 'AAPL'
api_key = '&apikey=K4pRVYD8DW8oeaxFButzBj1j7eQfZ4fr'
income_statement = requests.get("https://financialmodelingprep.com/api/v3/income-statement/{}?period=annual{}".format(ticker, api_key))
balance_sheet_statement = requests.get("https://financialmodelingprep.com/api/v3/balance-sheet-statement/{}?period=annual{}".format(ticker, api_key))

# print("INCOME STATEMENT")
# print("_________________________________")
# print("_________________________________")
# print("_________________________________")
# print(income_statement.json())
# print("BALANCE SHEET")
# print("_________________________________")
# print("_________________________________")
# print("_________________________________")
# print(balance_sheet_statement.json())

income_statement_obj = income_statement.json()[0]
balance_sheet_obj = balance_sheet_statement.json()[0]

print(income_statement_obj)
print("_________________________________")
print("_________________________________")
print("_________________________________")
print(balance_sheet_obj)

