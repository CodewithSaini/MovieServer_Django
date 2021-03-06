# Generated by Django 4.0.4 on 2022-05-03 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('released', models.DateField()),
                ('rated', models.CharField(max_length=5, null=True)),
                ('runtime', models.IntegerField()),
                ('plot', models.TextField(null=True)),
                ('genre', models.TextField(null=True)),
                ('actors', models.TextField(null=True)),
                ('directors', models.TextField(null=True)),
                ('writers', models.TextField(null=True)),
                ('awards', models.TextField(null=True)),
                ('poster', models.URLField(null=True)),
            ],
        ),
    ]
