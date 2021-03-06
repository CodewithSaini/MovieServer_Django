from datetime import datetime
from tkinter import CASCADE
from unicodedata import category
from django.contrib.auth.models import User
from django.db import models
from django.forms import CheckboxSelectMultiple
from setuptools import Require
from multiselectfield import MultiSelectField


# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

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
        max_length=7, choices=movie_rated, default='PG', blank=False)
    runtime = models.IntegerField(blank=False)
    plot = models.TextField(null=True)
    genre = MultiSelectField(
        max_length=60, choices=movie_genres, null=True)
    actors = models.CharField(max_length=500, null=True)
    directors = models.CharField(max_length=100, null=True)
    writers = models.CharField(max_length=100, null=True, blank=True)
    awards = models.CharField(max_length=100, null=True, blank=True)
    poster = models.URLField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collection = models.CharField(blank=True, default=0, max_length=20)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "-"+str(self.id)


class Review(models.Model):
    review_score = models.IntegerField()
    review_summary = models.TextField(max_length=20)
    full_review = models.TextField(max_length=300, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.review_score)+"-"+self.review_summary


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
