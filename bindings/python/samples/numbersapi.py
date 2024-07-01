import requests


def get_random_trivia():
    response = requests.get('http://numbersapi.com/random/trivia')
    print(response.text)
    return response.text
