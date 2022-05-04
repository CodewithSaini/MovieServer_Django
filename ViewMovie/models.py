from operator import truediv
from re import M
from tkinter import Widget
from django.db import models
from pkg_resources import require
from setuptools import Require

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=250, unique=True)
    released = models.DateField()
    rated = models.CharField(max_length=5, null=True)
    runtime = models.TextField()
    plot = models.TextField(null=True)
    genre = models.TextField(null=True)
    actors = models.TextField(null=True)
    directors = models.TextField(null=True)
    writers = models.TextField(null=True)
    awards = models.TextField(null=True)
    poster = models.URLField(null=True)

    def __str__(self):
        return self.title
