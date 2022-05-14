import datetime
from datetime import date
from datetime import timedelta
from email import message
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from ViewMovie.forms import UserInfoForm, UserLogInForm, AddMovieForm
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
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    if request.method == "POST" and searched_movies != 0 and "search_btn" in request.POST:
        if searched_movies == 'no movie':
            return redirect('/')
        else:
            if searched_movies.count() == 1:
                print("hi")
                return render(request, 'search.html', {'movies': searched_movies})
            elif searched_movies.count() > 1:
                return render(request, 'search.html', {'movies': searched_movies})

    content = Movie.objects.all().order_by('title')
    paginator = Paginator(content, 25)  # Show 25 contacts per page.
    print(content.count())
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    nums = "x"*movies.paginator.num_pages
    for movie in movies:
        print(movie.genre)
    return render(request, 'movies.html', {'movies': movies})


def log_in(request):
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    if request.method == "POST" and searched_movies != 0 and "search_btn" in request.POST:
        if searched_movies == 'no movie':
            return redirect('/')
        else:
            if searched_movies.count() == 1:
                print("hi")
                return render(request, 'search.html', {'movies': searched_movies})
            elif searched_movies.count() > 1:
                return render(request, 'search.html', {'movies': searched_movies})

    if request.method == 'POST':
        user_login_form = UserLogInForm(data=request.POST)
    else:
        user_login_form = UserLogInForm()

    return render(request, 'login.html', {'user_login_form': user_login_form})


def just_released(request):
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    if request.method == "POST" and searched_movies != 0 and "search_btn" in request.POST:
        if searched_movies == 'no movie':
            return redirect('/')
        else:
            if searched_movies.count() == 1:
                print("hi")
                return render(request, 'search.html', {'movies': searched_movies})
            elif searched_movies.count() > 1:
                return render(request, 'search.html', {'movies': searched_movies})

    today_date = date.today()
    past_date = today_date - timedelta(days=30)
    content = Movie.objects.filter(released__range=(past_date, today_date))
    paginator = Paginator(content, 25)  # Show 25 contacts per page.
    print(content.count())
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    nums = "x"*movies.paginator.num_pages
    return render(request, 'latestmovies.html', {'movies': movies, 'nums': nums})


def comming_soon(request):
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    if request.method == "POST" and searched_movies != 0 and "search_btn" in request.POST:
        if searched_movies == 'no movie':
            return redirect('/')
        else:
            if searched_movies.count() == 1:
                print("hi")
                return render(request, 'search.html', {'movies': searched_movies})
            elif searched_movies.count() > 1:
                return render(request, 'search.html', {'movies': searched_movies})

    today_date = date.today()
    future_date = today_date+timedelta(days=60)
    print(future_date)
    comming_soon_movies = Movie.objects.filter(
        released__range=(today_date, future_date))

    return render(request, 'commingsoon.html', {'movies': comming_soon_movies})


def movie_by_genre(request):
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    if request.method == "POST" and searched_movies != 0 and "search_btn" in request.POST:
        if searched_movies == 'no movie':
            return redirect('/')
        else:
            if searched_movies.count() == 1:
                print("hi")
                return render(request, 'search.html', {'movies': searched_movies})
            elif searched_movies.count() > 1:
                return render(request, 'search.html', {'movies': searched_movies})

    all_genres = []
    genres = Movie.movie_genres
    for genre in genres:
        all_genres.append(genre[0])
    return render(request, 'bygenre.html', {'genres': all_genres})


def one_genre_movies(request, genre):
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    if request.method == "POST" and searched_movies != 0 and "search_btn" in request.POST:
        if searched_movies == 'no movie':
            return redirect('/')
        else:
            if searched_movies.count() == 1:
                print("hi")
                return render(request, 'search.html', {'movies': searched_movies})
            elif searched_movies.count() > 1:
                return render(request, 'search.html', {'movies': searched_movies})

    print(genre)
    one_genre = Movie.objects.filter(genre__contains=genre)

    return render(request, 'search.html', {'movies': one_genre})


def movie_page(request, title):
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    if request.method == "POST" and searched_movies != 0 and "search_btn" in request.POST:
        if searched_movies == 'no movie':
            return redirect('/')
        else:
            if searched_movies.count() == 1:
                print("hi")
                return render(request, 'search.html', {'movies': searched_movies})
            elif searched_movies.count() > 1:
                return render(request, 'search.html', {'movies': searched_movies})

    movie = Movie.objects.get(title=title)
    actor = movie.actors.split(", ")
    print(actor)
    return render(request, 'moviepage.html', {"movie": movie, 'actors': actor})


def add_movie(request):
    print(request.POST)
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    if request.method == 'POST' and "add_movie_btn" in request.POST:
        add_movie_form = AddMovieForm(data=request.POST)
        if add_movie_form.is_valid():
            add_movie_form.save()
            print("Movie is added to the database.")
            return redirect('movies')
        else:
            print("hi")
            print(add_movie_form.errors.as_data())

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
        add_movie_form = AddMovieForm
        return render(request, 'addmovie.html', {'navbar': 'addmovie', 'add_movie_form': add_movie_form})


def register(request):
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    print(request.POST)
    if request.method == "POST" and searched_movies != 0 and "search_btn" in request.POST:
        if searched_movies == 'no movie':
            return redirect('register')
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


def update_movie(request, title):
    print(request.POST)
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    movie = Movie.objects.get(title=title)
    update_movie_form = AddMovieForm(instance=movie)
    if request.method == 'POST' and "add_movie_btn" in request.POST:
        update_movie_form = AddMovieForm(data=request.POST, instance=movie)
        if update_movie_form.is_valid():
            update_movie_form.save()
            print("Movie fields are updated!")
            return redirect('/movies/' + title)
        else:
            print("hi")
            print(update_movie_form.errors.as_data())
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
        add_movie_form = AddMovieForm
        return render(request, 'addmovie.html', {'navbar': 'addmovie', 'add_movie_form': update_movie_form})


def delete_movie(request, title):
    s_title = request.POST.get('search_title', "")
    searched_movies = search_movie(s_title)
    if request.method == "POST" and searched_movies != 0 and "search_btn" in request.POST:
        if searched_movies == 'no movie':
            return redirect('/')
        else:
            if searched_movies.count() == 1:
                print("hi")
                return render(request, 'search.html', {'movies': searched_movies})
            elif searched_movies.count() > 1:
                return render(request, 'search.html', {'movies': searched_movies})

    movie = Movie.objects.get(title=title)
    delete_movie_form = AddMovieForm(instance=movie)
    if request.method == 'POST' and "delete_btn_final" in request.POST:
        movie.delete()
        return redirect('movies')
    return render(request, 'delete.html', {'title': title, 'movie': movie})
