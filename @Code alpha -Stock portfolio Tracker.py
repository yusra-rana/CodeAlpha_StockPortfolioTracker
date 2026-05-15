
# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 200
}

total_investment = 0

print("📈 Stock Portfolio Tracker")
print("---------------------------")

# Taking input from user
while True:
    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"{stock_name} Investment Value: ${investment}")
    else:
        print("Stock not found!")

print("---------------------------")
print(f"Total Investment Value: ${total_investment}")

# Optional: Save result to file
file = open("portfolio.txt", "w")
file.write(f"Total Investment Value: ${total_investment}")
file.close()

print("Portfolio saved to portfolio.txt")

