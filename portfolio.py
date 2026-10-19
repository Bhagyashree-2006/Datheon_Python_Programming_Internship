import csv
import os
from datetime import datetime

# Practice kosam sample current prices.
# Ivi live stock prices kaavu.
current_prices = {
    "AAPL": 220.00,
    "MSFT": 430.00,
    "GOOGL": 175.00,
    "AMZN": 190.00,
}


def main():
    portfolio = []
    print("Stock Portfolio Performance Tracker")
    print("Available sample tickers:", ", ".join(current_prices))

    while True:
        ticker = input("\nStock ticker (finish cheyyadaniki DONE type cheyyi): ").strip().upper()

        if ticker == "DONE":
            break

        if ticker not in current_prices:
            print("Ticker sample list lo ledu. List lo unna ticker enter cheyyi.")
            continue

        try:
            buy_price = float(input("Share konna price: "))
            quantity = int(input("Enni shares konnavu?: "))

            if buy_price <= 0 or quantity <= 0:
                print("Price, shares rendu zero kanna ekkuva undali.")
                continue
        except ValueError:
            print("Price number-ga, shares whole number-ga enter cheyyi.")
            continue

        market_price = current_prices[ticker]
        invested = buy_price * quantity
        market_value = market_price * quantity
        gain_loss = market_value - invested
        gain_loss_percent = (gain_loss / invested) * 100

        portfolio.append({
            "ticker": ticker,
            "buy_price": buy_price,
            "market_price": market_price,
            "quantity": quantity,
            "invested": invested,
            "market_value": market_value,
            "gain_loss": gain_loss,
            "gain_loss_percent": gain_loss_percent,
        })

    if not portfolio:
        print("Portfolio entries levu. Program close avutondi.")
        return

    print("\n--- Portfolio Summary ---")
    for item in portfolio:
        print(
            f"{item['ticker']}: {item['quantity']} shares | "
            f"Value: ${item['market_value']:.2f} | "
            f"Gain/Loss: ${item['gain_loss']:.2f} "
            f"({item['gain_loss_percent']:.2f}%)"
        )

    total_invested = sum(item["invested"] for item in portfolio)
    total_value = sum(item["market_value"] for item in portfolio)
    total_gain_loss = total_value - total_invested

    print(f"\nTotal invested: ${total_invested:.2f}")
    print(f"Current portfolio value: ${total_value:.2f}")
    print(f"Total gain/loss: ${total_gain_loss:.2f}")

    file_name = "portfolio_summary.csv"
    file_exists = os.path.exists(file_name)

    with open(file_name, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "date", "ticker", "buy_price", "market_price",
                "quantity", "invested", "market_value",
                "gain_loss", "gain_loss_percent"
            ])

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for item in portfolio:
            writer.writerow([
                date,
                item["ticker"],
                f"{item['buy_price']:.2f}",
                f"{item['market_price']:.2f}",
                item["quantity"],
                f"{item['invested']:.2f}",
                f"{item['market_value']:.2f}",
                f"{item['gain_loss']:.2f}",
                f"{item['gain_loss_percent']:.2f}",
            ])

    print(f"\nResults {file_name} file lo save ayyayi.")


if __name__ == "__main__":
    main()