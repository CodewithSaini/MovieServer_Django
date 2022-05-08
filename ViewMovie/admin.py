from django.contrib import admin
from .import models
from ViewMovie.models import Movie, UserInfo
from django.contrib.auth.models import User
# Register your models here.


admin.site.register(Movie)
admin.site.register(UserInfo)
