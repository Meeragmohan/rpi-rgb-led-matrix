import requests

cryptoprice=""
def get_bitcoin_price_usd():
    response = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/btc.json")
    data = response.json()
    cryptoprice = "Bitcoin price in USD: " + str(round(data["btc"]["usd"], 2))
    return cryptoprice

print(get_bitcoin_price_usd())