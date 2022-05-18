from django.urls import path
from .import views


urlpatterns = [
    path('', views.home_page, name="home"),
    path('addmovie/', views.add_movie, name="addmovie"),
    path('movies/', views.movies, name="movies"),
    path('user/login/', views.log_user_in, name="login"),
    path('user/logout/', views.log_user_out, name="logout"),
    path('user/profile/', views.user_profile, name="profile"),
    path('justreleased/', views.just_released, name="justreleased"),
    path('commingsoon/', views.comming_soon, name="commingsoon"),
    path('bygenre/', views.movie_by_genre, name="bygenre"),
    path('movies/<str:title>/', views.movie_page, name="one_movie"),
    path('user/register/', views.register, name="register"),
    path('bygenre/<str:genre>', views.one_genre_movies, name="one_genre"),
    path('movies/update/<str:title>/', views.update_movie, name="update"),
    path('movies/delete/<str:title>/', views.delete_movie, name="delete"),
    path('movies/<str:title>/addreview/', views.addreview, name="reviewform")
]
