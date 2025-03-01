# 2. currency exchange
exchangerates = {}
with open("LA4B_Set and Dictionary/currency.csv") as file:
    next(file) 
    exchangerates = {line.split(",")[0]: (line.split(",")[1], float(line.split(",")[2])) for line in file}

amount = float(input("How much dollar do you have? "))
currency = input("What currency you want to have? ").upper()

if currency in exchangerates:
    name, rate = exchangerates[currency]
    print(f"\nDollar: {amount} USD")
    print(f"{name}: {amount * rate}")
else:
    print("Currency not found.")
