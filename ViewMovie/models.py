from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


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


class Review(models.Model):
    review_score = models.IntegerField()
    review_summary = models.TextField()
    movie_reviewed = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.review_summary
