from django.core.exceptions import ValidationError


def letters_numbers_underscores_validator(value):
    for ch in value:
        if not ch.isnumeric() and not ch.isalpha() and not ch == "_":
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

    # if not value.isidentifier():
    #     raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
