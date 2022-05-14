from django.contrib.auth.models import User
from django.db import models
from django.forms import CheckboxSelectMultiple
from pkg_resources import require
from setuptools import Require
from multiselectfield import MultiSelectField


# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Movie(models.Model):
    movie_rated = [
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('G', 'G'),
        ('R', 'R'),
        ('NC-17', 'NC-17')
    ]
    movie_genres = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Science Fiction', 'Science Fiction'),
        ('Animation', 'Animation'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Crime', 'Crime'),
        ('Thriller', 'Thriller'),
        ('Sports', 'Sports')
    ]

    title = models.CharField(max_length=250, unique=True)
    released = models.DateField()
    rated = models.CharField(
        max_length=7, choices=movie_rated, default='PG', null=True)
    runtime = models.IntegerField(blank=True)
    plot = models.TextField(null=True)
    genre = MultiSelectField(
        max_length=500, choices=movie_genres, null=True)
    actors = models.CharField(max_length=500, null=True)
    directors = models.CharField(max_length=500, null=True)
    writers = models.CharField(max_length=200, null=True, blank=True)
    awards = models.CharField(max_length=200, null=True, blank=True)
    poster = models.URLField(null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    review_score = models.IntegerField()
    review_summary = models.TextField()
    movie_reviewed = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.review_summary
