from django.contrib import admin
from .import models
from ViewMovie.models import Movie
# Register your models here.


admin.site.register(Movie)
