from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .validators import verify_letters_only, CheckMaxSizeInMb


class Profile(models.Model):
    first_name = models.CharField(validators=[MinLengthValidator(2),
                                              verify_letters_only],
                                  max_length=15)
    last_name = models.CharField(validators=[
        MinLengthValidator(2),
        verify_letters_only
    ],
        max_length=15)
    budget = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), ]
    )
    profile_image = models.ImageField(null=True,
                                      blank=True,
                                      upload_to='profile_images/',
                                      validators=[
                                          CheckMaxSizeInMb(5),
                                      ]
                                      )

    # ▪ Image field, optional. The picture is user.png (located in the resources) by default; if no image is uploaded)
    # ▪ The max size limit is 5MB (inclusive). Otherwise, raise ValidationError with the message: "Max file size is 5.00 MB"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Expense(models.Model):
    title = models.CharField(max_length=30)
    expense_image = models.URLField(verbose_name="Link to Image")
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        ordering = ("title", "-price")  # to avoid different sequence of items displayed in home page after each edit
