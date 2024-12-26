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


#https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=e60c7b56d19b53db3c996d3eef965a571649944a

def get_tinga_stock_prices(symbols):
    stockprices = " ***     "
    for symbol in symbols:
        url = f"https://api.tiingo.com/tiingo/daily/{symbol}/prices?token=e60c7b56d19b53db3c996d3eef965a571649944a"
        response = requests.get(url)
        data = response.json()
        if data:
            try:
                price = data[0]["close"]
                stockprices += symbol + ": " + str(price) + "; change: "
                stockprices += str(round((data[0]["close"]-data[0]["open"])*100/data[0]["close"],2)) + "%      "
            except Exception as e:
                print(f"Error occurred: {e}")
                continue
        elif data:
            return "*** Stock prices unavailable at the moment. ***" 
    return stockprices + " *** "

print(get_tinga_stock_prices(symbols))