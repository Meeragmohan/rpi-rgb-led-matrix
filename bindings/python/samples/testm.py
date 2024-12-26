import json
import random

def get_random_movie():
    with open('./movies/movies.json') as file:
        data = json.load(file)
        random_movie = random.choice(data)
        print(random_movie)
        return random_movie
    
get_random_movie()
