from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=30)  # - Character field with max length of 30 characters
    last_name = models.CharField(max_length=30)  # - Character field with max length of 30 characters
    image_url = models.URLField()  # - URL field


class Book(models.Model):
    title = models.CharField(max_length=30)  # - Character field with max length of 30 characters
    description = models.TextField()  # - Text field
    image = models.URLField()  # - URL field
    type = models.CharField(max_length=30)  # - Character field with max length of 30 characters
