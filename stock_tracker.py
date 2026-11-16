stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

portfolio = []
total_investment = 0

print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when you are finished.\n")

while True:
    stock = input("Enter stock symbol: ").upper().strip()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found in list. Try again.\n")
        continue

    qty_input = input(f"Enter quantity for {stock}: ").strip()
    if not qty_input.isdigit() or int(qty_input) <= 0:
        print("Please enter a valid positive number.\n")
        continue

    qty = int(qty_input)
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    portfolio.append((stock, qty, price, value))
    print(f"Added {qty} shares of {stock} (${value})\n")

print("\n--- Portfolio Summary ---")
for item in portfolio:
    print(f"{item[0]}: {item[1]} shares x ${item[2]} = ${item[3]}")
print(f"Total Investment Value: ${total_investment}")

save = input("\nDo you want to save this to a file? (txt/csv/no): ").lower().strip()

if save == "txt":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        for item in portfolio:
            f.write(f"{item[0]}: {item[1]} shares x ${item[2]} = ${item[3]}\n")
        f.write(f"Total Investment Value: ${total_investment}\n")
    print("Saved to portfolio.txt")

elif save == "csv":
    with open("portfolio.csv", "w") as f:
        f.write("Stock,Quantity,Price,Total\n")
        for item in portfolio:
            f.write(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")
        f.write(f"Total,,,{total_investment}\n")
    print("Saved to portfolio.csv")