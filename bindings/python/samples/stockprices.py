import requests

symbols = ["TEAM", "AAPL", "GOOGL"]
#add bitcoin price also
def get_stock_prices(symbols):
    stockprices = " *** "
    for symbol in symbols:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&apikey=LWEKHPEQ4SR9KTHU&symbol={symbol}"
        response = requests.get(url)
        data = response.json()
        
        if not data["Global Quote"]:
            return "*** Stock prices unavailable at the moment. ***" 
        
        else:
            #if data["Information"]:
            #return "*** Stock prices unavailable at the moment. ***"
        
            symbol_name = data["Global Quote"]["01. symbol"]
            price = data["Global Quote"]["05. price"]
            change_percent = data["Global Quote"]["10. change percent"]

            stockprices += symbol_name + " " + price + " " + change_percent + " " + symbol_name + " *** "
    return stockprices

#print(get_stock_prices(symbols))