import requests


def get_random_trivia(basepath):
    response = requests.get('http://numbersapi.com/random/trivia')
    print(response.text)
    with open(basepath + 'trivia/numbertrivia.txt', 'a') as file:
        file.write(response.text + '\n')
    return response.text
