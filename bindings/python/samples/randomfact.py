import requests


url = "http://api.fungenerators.com/fact/random"
query = "Amazon"
headers = {
    "accept": "application/json",
    "X-Fungenerators-Api-Secret": "api_key"
}

response = requests.get(url, params={"query": query}, headers=headers)
print(response.json())