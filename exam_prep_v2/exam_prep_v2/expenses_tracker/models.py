from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_prep_v2.expenses_tracker.validators import alpha_only_validator, CheckMaxSizeInMb


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
        validators=(MinLengthValidator(2), alpha_only_validator)  # validators as list or tuple
    )

    last_name = models.CharField(
        max_length=15,
        validators=(MinLengthValidator(2), alpha_only_validator)  # validators as list or tuple
    )

    budget = models.FloatField(
        default=0,
        validators=(MinValueValidator(0),)
    )

    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='profile_images/',
        validators=(CheckMaxSizeInMb,),
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Expense(models.Model):
    title = models.CharField(max_length=30)

    expense_image = models.URLField(
        verbose_name="Link to Image"
    )

    description = models.TextField(
        null=True, blank=True,
    )

    price = models.FloatField()

    def __str__(self):
        return f"{self.title} {self.price}"
