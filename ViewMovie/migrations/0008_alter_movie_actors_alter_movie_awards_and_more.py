# Generated by Django 4.0.4 on 2022-05-13 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViewMovie', '0007_alter_movie_rated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='awards',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writers',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
