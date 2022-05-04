from django.urls import path
from .import views


urlpatterns = [
    path('', views.home_page, name="home"),
    path('addmovie/', views.add_movie, name="addmovie"),
    path('movies', views.movies, name="movies")
]
