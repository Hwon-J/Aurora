# Generated by Django 3.2.13 on 2023-05-21 12:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_alter_movie_liked_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watched_users',
            field=models.ManyToManyField(blank=True, related_name='watched_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
