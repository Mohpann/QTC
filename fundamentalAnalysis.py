# Connor Hunter

import requests
ticker = 'AAPL'
api_key = '&apikey=K4pRVYD8DW8oeaxFButzBj1j7eQfZ4fr'
income_statement = requests.get("https://financialmodelingprep.com/api/v3/income-statement/{}?period=annual{}".format(ticker, api_key))
balance_sheet_statement = requests.get("https://financialmodelingprep.com/api/v3/balance-sheet-statement/{}?period=annual{}".format(ticker, api_key))
cash_flow_statement = requests.get("https://financialmodelingprep.com/api/v3/cash-flow-statement/{}?period=annual{}".format(ticker, api_key))

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
cash_flow_obj = cash_flow_statement.json()[0]

print("INCOME STATEMENT")
print(income_statement_obj)
print("_________________________________")
print("_________________________________")
print("_________________________________")
print("BALANCE SHEET")
print(balance_sheet_obj)
print("_________________________________")
print("_________________________________")
print("_________________________________")
print("CASH FLOW")
print(cash_flow_obj)