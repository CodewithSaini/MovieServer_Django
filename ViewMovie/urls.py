from django.urls import path
from .import views


urlpatterns = [
    path('', views.home_page, name="home"),
    path('addmovie/', views.add_movie, name="addmovie"),
    path('movies/', views.movies, name="movies"),
    path('login/', views.log_in, name="login"),
    path('latestmovies/', views.latest_movies, name="latestmovies"),
    path('commingsoon/', views.comming_soon, name="commingsoon"),
    path('bygenre/', views.movie_by_genre, name="bygenre"),
    path('movies/<str:title>/', views.movie_page, name="movies"),
    path('user/register/', views.register, name="register")
]
