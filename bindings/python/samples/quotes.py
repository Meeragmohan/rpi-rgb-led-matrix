import json
import random

# Read the quotes.json file
def get_random_quote():
    with open('/home/cyclops/Projects/rpi-rgb-led-matrix/bindings/python/samples/quoteslist/quotes.json') as file:
        quotes_json = json.load(file)

# Extract a random quote
    random_quote = random.choice(quotes_json["quotes"])

# return the random quote
    random_quote = "Quote of the hour: " + random_quote["quote"] + " - " + random_quote["author"]
    return random_quote
