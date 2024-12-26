import json
import random
import requests

def get_random_movie(basepath):
    with open(basepath+'movies/movies.json') as file:
        data = json.load(file)
        random_movie = random.choice(data)
        print(random_movie)
        return random_movie

def get_movie_poster(imdbid, basepath):
    url = f"https://img.omdbapi.com/?i={imdbid}&apikey=6ecf17ce"
    response = requests.get(url)

    if response.status_code == 200:
        file_path = basepath + "movies/movieposters/"+imdbid+".jpg"
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return file_path
    else:
        return None
