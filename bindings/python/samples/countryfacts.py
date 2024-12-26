import json
import random

countrycapital=""
def print_random_country():
    # Read countries.json file
    with open('/home/cyclops/Projects/rpi-rgb-led-matrix/bindings/python/samples/countries/countries.json') as file:
        data = json.load(file)

    # Select one random element from countries json array
    random_country = random.choice(data)
    print(random_country)
    # Print country name and capitals
    countrycapital="Capital of " + random_country['name']['common'] + " is "
    for capital in random_country['capital']:
        countrycapital = countrycapital + capital
    #print(random_country['flags']['png'])
    return {"country-capital":countrycapital,"country-name":random_country['name']['common']}
#print(print_random_country())