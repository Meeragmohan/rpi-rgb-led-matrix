import json
import random

countryinfo=""
def print_random_country():
    # Read countries.json file
    with open('/home/cyclops/Projects/rpi-rgb-led-matrix/bindings/python/samples/countries/countries.json') as file:
        data = json.load(file)

    # Select one random element from countries json array
    random_country = random.choice(data)

    # Print country name and capitals
    countryinfo="Capital of " + random_country['name']['common'] + " is "
    for capital in random_country['capital']:
        countryinfo = countryinfo + capital
    #print(random_country['flags']['png'])
    return countryinfo

print(print_random_country())