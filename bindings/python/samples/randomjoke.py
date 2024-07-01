import requests
import re

def get_random_joke():
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'text/plain'})
    response_text = response.text
    response_text = re.sub(r'[^\x00-\x7F]+', '', response_text)
    response_text = re.sub(r'[^\x00-\x7F]+', '', response_text)
    joke =  "Joke of the hour: " + response_text
    return joke