

import os
import json
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieServer.settings')

django.setup()
# ______________________________________________________________
months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}
from ViewMovie.models import Movie
with open("movie-data/movie-data-100.json") as json_file:
    movies = json.load(json_file)
    for mov in movies:
        posted_date = mov['Released'].split(' ')
        released_date = datetime.date(
            int(posted_date[2]), months[posted_date[1]], int(posted_date[0]))
        print(released_date)
        new_movie = Movie(title=mov['Title'],
                          released=released_date,
                          rated=mov['Rated'],
                          runtime=mov['Runtime'],
                          plot=mov['Plot'],
                          genre=mov['Genre'],
                          actors=mov['Actors'],
                          directors=mov['Director'],
                          writers=mov['Writer'],
                          awards=mov['Awards'],
                          poster=mov['Poster'],
                          )
        new_movie.save()

if __name__ == '__main__':
    print("Populating the movies!")
    print("All movies added th the database successfully!")
