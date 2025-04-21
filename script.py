import requests

def get_usdt_dzd_buy_offers():
    url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "asset": "USDT",
        "fiat": "DZD",
        "merchantCheck": False,
        "page": 1,
        "rows": 20,
        "payTypes": [],
        "tradeType": "BUY"  # People who want to BUY USDT
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    return data["data"]

def calculate_prices(offers):
    prices = [float(offer["adv"]["price"]) for offer in offers]

    average_price = sum(prices) / len(prices)
    highest_price = max(prices)
    lowest_price = min(prices)

    return average_price, highest_price, lowest_price

def convert_dzd_to_usdt(dzd_amount, average_price):
    return dzd_amount / average_price

def main():
    offers = get_usdt_dzd_buy_offers()
    average, high, low = calculate_prices(offers)

    print(f"Average Price (Top 20 Buyers): {average:.2f} DZD")
    print(f"Highest Price: {high:.2f} DZD")
    print(f"Lowest Price: {low:.2f} DZD")

    try:
        dzd_amount = float(input("Enter amount in DZD to convert to USDT: "))
        usdt_amount = convert_dzd_to_usdt(dzd_amount, average)
        print(f"{dzd_amount:.2f} DZD ≈ {usdt_amount:.4f} USDT at average price")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
