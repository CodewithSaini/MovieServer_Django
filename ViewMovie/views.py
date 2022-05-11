import datetime
from datetime import date
from datetime import timedelta
from email import message
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from ViewMovie.forms import UserInfoForm, UserLogInForm
from ViewMovie.models import Movie
from django.contrib import messages
# Create your views here.


def search_movie(title):
    if len(title) > 0:
        print(len(title))
        if Movie.objects.filter(title__contains=title):
            mov = Movie.objects.filter(title__contains=title)
            return mov
        else:
            return 'no movie'
    else:
        return 0


def home_page(request):
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    print(request.POST)
    if request.method == "POST" and searched_movies != 0 and "search_btn" in request.POST:
        if searched_movies == 'no movie':
            return redirect('/')
        else:
            if searched_movies.count() == 1:
                print("hi")
                return render(request, 'search.html', {'movies': searched_movies})
            elif searched_movies.count() > 1:
                return render(request, 'search.html', {'movies': searched_movies})

    else:
        today_date = datetime.date.today()
        future_date = today_date + timedelta(days=30)
        past_date = today_date - timedelta(days=60)
        featured_movie = Movie.objects.filter(
            released__range=(past_date, future_date))

        print(featured_movie)
        return render(request, 'home.html', {'navbar': 'home', 'feature_movie': featured_movie, 'home': "home"})


def movies(request):
    content = Movie.objects.all().order_by('title')
    paginator = Paginator(content, 25)  # Show 25 contacts per page.
    print(content.count())
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    nums = "x"*movies.paginator.num_pages

    return render(request, 'movies.html', {'movies': movies, 'nums': nums})


def log_in(request):
    if request.method == 'POST':
        user_login_form = UserLogInForm(data=request.POST)
    else:
        user_login_form = UserLogInForm()

    return render(request, 'login.html', {'user_login_form': user_login_form})


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
    # print(x)
    different_genres = []
    for genre in x:
        y = genre['genre'].split(", ")
        for g in y:
            if g not in different_genres:
                different_genres.append(g)
    print(different_genres)
    #messages.success(request, 'You are at genres!')
    return render(request, 'bygenre.html', {'genres': different_genres})


def movie_page(request, title):
    movie = Movie.objects.get(title=title)
    actor = movie.actors.split(", ")
    print(actor)
    return render(request, 'moviepage.html', {"movie": movie, 'actors': actor})


def add_movie(request):
    genres = Movie.objects.values('genre').distinct()
    x = list(genres)
    # print(x)
    different_genres = []
    for genre in x:
        y = genre['genre'].split(", ")
        for g in y:
            if g not in different_genres:
                different_genres.append(g)
    print(different_genres)
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
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    print(request.POST)
    if request.method == "POST" and searched_movies != 0 and "search_btn" in request.POST:
        if searched_movies == 'no movie':
            return redirect('/')
        else:
            if searched_movies.count() == 1:
                print("hi")
                return render(request, 'search.html', {'movies': searched_movies})
            elif searched_movies.count() > 1:
                return render(request, 'search.html', {'movies': searched_movies})

    else:
        if request.method == "POST" and 'register_btn' in request.POST:
            user_form = UserInfoForm(data=request.POST)
            if user_form.is_valid():
                print(request.POST)
                user_form.save()
        else:
            user_form = UserInfoForm()

    return render(request, 'register.html', {'navbar': 'register', 'user_form': user_form})
