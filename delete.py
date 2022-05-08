


import os
import json
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieServer.settings')

django.setup()
from ViewMovie.models import Movie

def delete_alldata():
    all_movies = Movie.objects.all()
    for movie in all_movies:
        if(movie.genre.startswith("[")):
            print(movie.genre)
            movie.delete()


if __name__ == '__main__':
    delete_alldata()
    print("Deleting all the movies!")
    print("All movies deleted from the database successfully!")
