import datetime
from django.core.paginator import Paginator
from platform import release
from django.shortcuts import render
from django.http import HttpResponse
from .import models
from ViewMovie.models import Movie
# Create your views here.


def home_page(request):
    return render(request, 'home.html', {'navbar': 'home'})


def movies(request):
    content = Movie.objects.all().order_by('title')
    paginator = Paginator(content, 25)  # Show 25 contacts per page.
    print(content.count())
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    return render(request, 'movies.html', {'movies': movies})


def log_in(request):
    return render(request, 'login.html', {'navbar': 'login'})


def latest_movies(request):
    latest_movies = Movie.objects.all().order_by('-released')
    return render(request, 'latestmovies.html', {'movies': latest_movies})


def comming_soon(request):
    latest_movies = Movie.objects.filter()
    return render(request, 'latestmovies.html', {})


def movie_by_genre(request):
    latest_movies = Movie.objects.filter()
    return render(request, 'bygenre.html', {})


def movie_page(request, title):
    print(title)
    movie = Movie.objects.get(title=title)
    return render(request, 'moviepage.html', {"movie": movie})


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
