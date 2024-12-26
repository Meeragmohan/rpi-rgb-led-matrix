import requests

cryptoprice=""
def get_bitcoin_price_usd():
    response = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
    data = response.json()
    cryptoprice = "Bitcoin price in USD: " + data["data"]["rates"]["USD"]
    return cryptoprice

#print(get_bitcoin_price_usd())