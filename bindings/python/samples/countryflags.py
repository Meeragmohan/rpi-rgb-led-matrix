import requests
import os

def download_flag(url, filename):
    if not os.path.exists(filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def listallcountries():
    api_call = requests.get("https://www.thesportsdb.com/api/v1/json/3/all_countries.php")
    storage = api_call.json()
    for country in storage["countries"]:
        flag_url = country['flag_url_32']
        print(flag_url)
        filename = os.path.join('./flags', os.path.basename(flag_url))
        download_flag(flag_url, filename)
        print(f"Downloaded flag for {country['name_en']}")
        

listallcountries()