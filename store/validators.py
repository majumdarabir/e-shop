from django.core.exceptions import ValidationError


def check_valid_ratings(value):
    if not (value >= 0 and value <= 5):
        raise ValidationError("Invalid Rating")
