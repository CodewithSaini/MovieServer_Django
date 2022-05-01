
import json


with open('../movie-data/movie-data-10.json') as json_file:
    movies = json.load(json_file)
    for movie in movies:
        print(movie['Title'])
