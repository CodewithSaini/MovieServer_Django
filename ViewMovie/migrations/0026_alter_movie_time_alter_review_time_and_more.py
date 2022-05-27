# Generated by Django 4.0.4 on 2022-05-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViewMovie', '0025_watchlist_delete_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='time',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='time',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='time',
            field=models.DateTimeField(editable=False),
        ),
    ]