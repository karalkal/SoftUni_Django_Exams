from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def alpha_only_validator(value):
    if not value.isalpha():
        raise ValidationError("Ensure this value contains only letters.")


@deconstructible
class CheckMaxSizeInMb:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError('Max file size is 5.00 MB')
