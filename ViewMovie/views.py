from collections import namedtuple
import datetime
from itertools import chain
from operator import attrgetter
from django.utils import timezone
from django.contrib import messages
from sqlite3 import Date
from django.template.defaulttags import register
from datetime import date, tzinfo
from datetime import timedelta
from time import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from ViewMovie.forms import UserInfoForm, AddMovieForm, ReviewForm
from ViewMovie.models import Movie, Review, UserInfo, User, WatchList
from django.contrib import messages
from .helper_function import get_event_date
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
            messages.success(request, "No matching movie found!")
            return redirect('/')
        else:
            if searched_movies.count() == 1:
                messages.success(request, "Here is the matched movie!")
                return render(request, 'search.html', {'movies': searched_movies})
            elif searched_movies.count() > 1:
                messages.success(request, "Here are the matched movies!")
                return render(request, 'search.html', {'movies': searched_movies})

    else:
        today_date = datetime.date.today()
        future_date = today_date + timedelta(days=30)
        past_date = today_date - timedelta(days=60)
        featured_movie = Movie.objects.filter(
            released__range=(past_date, future_date))
        return render(request, 'home.html', {'navbar': 'home', 'feature_movie': featured_movie, 'home': "home"})


def movies(request):

    content = Movie.objects.all().order_by('title')
    paginator = Paginator(content, 25)  # Show 25 contacts per page.
    print(content.count())
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    nums = "x"*movies.paginator.num_pages
    for movie in movies:
        print(movie.genre)
    return render(request, 'movies.html', {'movies': movies, 'navbar': 'movies', 'nums': nums})


def log_user_in(request):
    if request.method == 'POST' and "login_btn" in request.POST:
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print(user)
            messages.success(request, "You have successfully Logged In.")
            return redirect('profile')

        else:
            messages.error(
                request, "You have entered invalid credentials. Please try again")
            return redirect('login')
    else:

        return render(request, 'login.html', {'navbar': 'login'})


@login_required
def log_user_out(request):
    logout(request)
    messages.success(request, "You are successfully logout!")
    return redirect('login')


def top_50_movies(request):
    
    content = Movie.objects.all().order_by("-collection")[:50]
    paginator = Paginator(content, 25)  # Show 25 contacts per page.
    print(content.count())
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    nums = "x"*movies.paginator.num_pages
    return render(request, 'top50.html', {'movies': movies, 'nums': nums})


def just_released(request):
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
    today_date = date.today()
    future_date = today_date+timedelta(days=60)
    print(future_date)
    comming_soon_movies = Movie.objects.filter(
        released__range=(today_date, future_date))

    return render(request, 'commingsoon.html', {'movies': comming_soon_movies})


def movie_by_genre(request):
    all_genres = []
    genres = Movie.movie_genres
    for genre in genres:
        all_genres.append(genre[0])
    return render(request, 'bygenre.html', {'genres': all_genres})


def one_genre_movies(request, genre):
    print(genre)
    one_genre = Movie.objects.filter(genre__contains=genre)
    messages.success(request, "All the {} movies are here!".format(genre))
    return render(request, 'search.html', {'movies': one_genre})


def movie_page(request, title):
    in_watchlist = False
    average_rating = 0
    movie = Movie.objects.get(title=title)
    if movie.runtime:
        run_hour = movie.runtime//60
        run_min = movie.runtime % 60
    reviews = movie.review_set.all().order_by('-time')
    if reviews.count() > 0:
        for review in reviews:
            average_rating += review.review_score
        average_rating = round(average_rating/reviews.count(), 1)
    m_writers = movie.writers.split(", ")
    actor = movie.actors.split(", ")
    m_directors = movie.directors.split(", ")
#############################add to watchlist ###################################################
    if request.user.is_authenticated:
        already_in_watchlist = WatchList.objects.all().filter(
            user=request.user, movie=movie)
        user_watchlist = WatchList.objects.all().filter(user=request.user)
        print(user_watchlist.count())
        if not already_in_watchlist:
            in_watchlist = False
            if user_watchlist.count() < 5 and request.method == 'POST' and "add_to_watchlist" in request.POST:
                watchlist_movie = WatchList(
                    user=request.user, movie=movie)
                watchlist_movie.save()
                messages.success(
                    request, "{} movie has added to your watchlist".format(movie.title))
                in_watchlist = True

            else:
                if user_watchlist.count() >= 5:
                    messages.error(request, "Your watchlist is already full!")
        else:
            in_watchlist = True
            print("Movie is already in User's Watchlist!")
            if already_in_watchlist and request.method == 'POST' and "remove_from_watchlist" in request.POST:
                already_in_watchlist.delete()
                messages.success(
                    request, "{} movie has removed from your watchlist".format(movie.title))
                in_watchlist = False
            else:
                print("Movie is not in your Watchlist!")
    if request.user.is_authenticated:
        if request.method == 'POST':
            for fields in request.POST:
                if fields.startswith("moviepagereview"):
                    r_movie_title = fields.split(",")[1]
                    r_movie = Movie.objects.get(title=r_movie_title)
                    f_review = fields.split(",")[2]
                    review_to_be_deleted = Review.objects.get(
                        movie=r_movie, user=request.user, full_review=f_review)
                    if review_to_be_deleted:
                        review_to_be_deleted.delete()
                        messages.success(request, "{} review has been deleted!".format(
                            review_to_be_deleted.review_summary))
                        return redirect("/movies/"+str(title))

    elif not request.user.is_authenticated and "add_to_watchlist" in request.POST:
        return render(request, 'loginrequired.html', {})

    return render(request, 'moviepage.html', {"directors": m_directors, "average_rating": average_rating, "writers": m_writers, "hour": run_hour, "min": run_min, "movie": movie, 'actors': actor, 'reviews': reviews, 'in_watchlist': in_watchlist})


def add_movie(request):
    if request.user.is_authenticated:
        print(request.POST)
        s_title = request.POST.get('search_title', "")
        searched_movies = search_movie(s_title)
        if request.method == 'POST' and "add_movie_btn" in request.POST:
            add_movie_form = AddMovieForm(data=request.POST)
            if add_movie_form.is_valid():
                new_movie = add_movie_form.save(commit=False)
                new_movie.user = request.user
                new_movie.save()
                messages.success(
                    request, "{} movie is added to the database!".format(new_movie.title))
                print("Movie is added to the database.")
                return redirect('movies')
            else:
                print(add_movie_form.errors.as_data())

        else:
            add_movie_form = AddMovieForm
            return render(request, 'addmovie.html', {'navbar': 'addmovie', 'add_movie_form': add_movie_form})
    else:
        return render(request, 'loginrequired.html', {})


def register_user(request):

    if request.method == "POST" and 'register_btn' in request.POST:
        user_form = UserInfoForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, "You are successfully register!")
        else:
            messages.error(request, user_form.errors)
    else:
        user_form = UserInfoForm()

    return render(request, 'register.html', {'navbar': 'register', 'user_form': user_form})


def update_movie(request, title):
    if request.user.is_authenticated:
        movie = Movie.objects.get(title=title)
        update_movie_form = AddMovieForm(instance=movie)
        if request.method == 'POST' and "add_movie_btn" in request.POST:
            update_movie_form = AddMovieForm(data=request.POST, instance=movie)
            if update_movie_form.is_valid():
                update_movie_form.save()
                messages.success(request, "Movie fields are updated!")
                return redirect('/movies/' + title)
            else:
                print(update_movie_form.errors.as_data())

        else:
            return render(request, 'addmovie.html', {'navbar': 'addmovie', 'add_movie_form': update_movie_form})
    else:

        return render(request, 'loginrequired.html', {})


def delete_movie(request, title):
    if request.user.is_authenticated:
        movie = Movie.objects.get(title=title)
        delete_movie_form = AddMovieForm(instance=movie)
        if request.method == 'POST' and "delete_btn_final" in request.POST:
            movie.delete()
            messages.success(request, "{} has been deleted!".format(title))
            return redirect('movies')
        return render(request, 'delete.html', {'title': title, 'movie': movie})
    else:
        return render(request, 'loginrequired.html', {})


def addreview(request, title):
    if request.user.is_authenticated:
        movie = Movie.objects.get(title=title)
        if request.user:
            user = User.objects.get(username=request.user)
            print(user)
        if request.method == 'POST' and "add_review_btn" in request.POST:
            reviewform = ReviewForm(data=request.POST)
            if reviewform.is_valid():
                review = reviewform.save(commit=False)
                review.movie = movie
                review.user = user
                review.save()
                messages.success(
                    request, "You added a new review for {}!".format(title))
                return redirect('/movies/'+title)
        else:
            reviewform = ReviewForm()
        return render(request, 'reviewform.html', {'reviewform': reviewform, 'title': title})
    else:
        return render(request, 'loginrequired.html', {'title': title})


def user_profile(request):
    if request.user.is_authenticated:
        current_user_movies = Movie.objects.all().filter(
            user=request.user).order_by('title')
        current_user_reviews = Review.objects.all().filter(
            user=request.user).order_by('-time')
        current_user_watchlist = WatchList.objects.all().filter(
            user=request.user)
        movies_added = Movie.objects.all()
        reviews = Review.objects.all()
        sorted_timeline = sorted(
            chain(movies_added, reviews), key=attrgetter('time'), reverse=True)
        if request.method == "POST":
            for fields in request.POST:
                if fields.startswith('review'):
                    f_review = fields.split(",")[1]
                    r_movie = fields.split(',')[2]
                    print(f_review)
                    print(r_movie)
                    review_movie = Movie.objects.get(title=r_movie)
                    review_to_be_deleted = Review.objects.get(
                        full_review=f_review, movie=review_movie, user=request.user)
                    messages.success(request, "{} review has been deleted!".format(
                        review_to_be_deleted.review_summary))
                    review_to_be_deleted.delete()
                elif fields.startswith('watchlist'):
                    m_title = fields.split(',')[1]
                    w_movie = Movie.objects.get(title=m_title)
                    watchlist_movie_to_be_deleted = WatchList.objects.get(
                        movie=w_movie, user=request.user)
                    if watchlist_movie_to_be_deleted:
                        watchlist_movie_to_be_deleted.delete()
                        messages.success(
                            request, "{} movie has removed from your watchlist".format(w_movie.title))
        for obj in sorted_timeline:
            obj.event_time = get_event_date(obj.time)
            if hasattr(obj, "title"):
                obj.type = "movie"
            # print(obj.event_time)

    else:
        return redirect('login')
    return render(request, 'profile.html', {'timeline': sorted_timeline, 'movies': current_user_movies, 'watchlist': current_user_watchlist, 'reviews': current_user_reviews})
