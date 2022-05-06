import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .import models
from ViewMovie.models import Movie
# Create your views here.


def home_page(request):
    return render(request, 'home.html', {'navbar': 'home'})


def movies(request):
    content = Movie.objects.all()
    print(content)
    return render(request, 'movies.html', {'movies': content})


def log_in(request):
    return render(request, 'login.html', {'navbar': 'login'})


def add_movie(request):
    if request.method == 'POST':
        posted_movie = request.POST.dict()
        posted_date = posted_movie['released'].split('-')
        released_date = datetime.date(
            int(posted_date[0]), int(posted_date[1]), int(posted_date[2]))
        print(posted_movie['released'].split('-'))
        new_movie = Movie(title=posted_movie['title'],
                          released=released_date,
                          rated=posted_movie['rated'],
                          runtime=posted_movie['runtime']+" min",
                          plot=posted_movie['plot'],
                          genre=posted_movie['genre'],
                          actors=posted_movie['actors'],
                          directors=posted_movie['directors'],
                          writers=posted_movie['writers'],
                          awards=posted_movie['awards'],
                          poster=posted_movie['poster'],
                          )
        print(new_movie)
        new_movie.save()
    return render(request, 'addmovie.html', {'navbar': 'addmovie'})
