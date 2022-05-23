from django.contrib import admin
from .import models
from ViewMovie.models import Movie, UserInfo, Review, WatchList
from django.contrib.auth.models import User
# Register your models here.


admin.site.register(Movie)
admin.site.register(UserInfo)
admin.site.register(Review)
admin.site.register(WatchList)
