# Generated by Django 4.0.4 on 2022-05-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViewMovie', '0026_alter_movie_time_alter_review_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]