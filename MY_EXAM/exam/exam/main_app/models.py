from django.db import models

from django.core.validators import MinLengthValidator, MinValueValidator
from exam.main_app.validators import letters_numbers_underscores_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2),
                    letters_numbers_underscores_validator, ]
    )
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} {self.age}"


class Album(models.Model):
    POP_MUSIC = ("Pop Music", "Pop Music")
    JAZZ_MUSIC = ("Jazz Music", "Jazz Music")
    R_AND_B_MUSIC = ("R&B Music", "R&B Music")
    ROCK_MUSIC = ("Rock Music", "Rock Music")
    COUNTRY_MUSIC = ("Country Music", "Country Music")
    DANCE_MUSIC = ("Dance Music", "Dance Music")
    HIP_HOP_MUSIC = ("Hip Hop Music", "Hip Hop Music")
    OTHER = ("Other", "Other")
    GENRE_CHOICES = [POP_MUSIC, JAZZ_MUSIC, R_AND_B_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER]

    album_name = models.CharField(max_length=30, unique=True, verbose_name="Album Name")
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(verbose_name="Image URL")
    price = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.album_name} {self.artist}"
