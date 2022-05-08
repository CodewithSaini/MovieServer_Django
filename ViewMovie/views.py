from calendar import different_locale
import datetime
from datetime import date
from datetime import timedelta
from email import message
from django.core.paginator import Paginator
from platform import release
from django.shortcuts import render
from django.http import HttpResponse
from ViewMovie.forms import UserInfoForm
from .import models
from ViewMovie.models import Movie
from django.contrib import messages
# Create your views here.


def home_page(request):
    return render(request, 'home.html', {'navbar': 'home'})


def movies(request):
    content = Movie.objects.all().order_by('title')
    paginator = Paginator(content, 25)  # Show 25 contacts per page.
    print(content.count())
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    nums = "x"*movies.paginator.num_pages
    return render(request, 'movies.html', {'movies': movies, 'nums': nums})


def log_in(request):
    return render(request, 'login.html', {'navbar': 'login'})


def latest_movies(request):
    content = Movie.objects.all().order_by('-released')
    paginator = Paginator(content, 25)  # Show 25 contacts per page.
    print(content.count())
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    nums = "x"*movies.paginator.num_pages
    return render(request, 'latestmovies.html', {'movies': movies, 'nums': nums})


def comming_soon(request):
    today_date = date.today()
    future_date = today_date+timedelta(days=60)
    print(future_date)
    comming_soon_movies = Movie.objects.filter(
        released__range=(today_date, future_date))

    return render(request, 'commingsoon.html', {'movies': comming_soon_movies})


def movie_by_genre(request):
    genres = Movie.objects.values('genre').distinct()
    x = list(genres)
    different_genres = []
    for genre in x:
        different_genres.append(genre['genre'])
    messages.success(request, 'You are at genres!')
    return render(request, 'bygenre.html', {'genres': different_genres})


def movie_page(request, title):
    print(title)
    movie = Movie.objects.get(title=title)
    return render(request, 'moviepage.html', {"movie": movie})


def add_movie(request):
    genres = Movie.objects.values('genre').distinct()
    x = list(genres)
    different_genres = []
    for genre in x:
        different_genres.append(genre['genre'])
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
    return render(request, 'addmovie.html', {'navbar': 'addmovie', 'genres': different_genres})


def register(request):
    if request.method == "POST":
        user_form = UserInfoForm(data=request.POST)
    else:
        user_form = UserInfoForm()

    return render(request, 'register.html', {'user_form': user_form})
