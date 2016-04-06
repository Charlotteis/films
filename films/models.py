from django.db import models


class Film(models.Model):
    name = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField()
    slug = models.SlugField(unique=True)
