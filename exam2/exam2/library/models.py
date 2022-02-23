from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image_url = models.URLField()


class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()  # - Text field
    image = models.URLField()  # - URL field
    type = models.CharField(max_length=30)
