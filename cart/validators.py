from django.core.exceptions import ValidationError
from django.utils import timezone


def item_count_ge_zero(count):
    if count <= 0:
        raise ValidationError("Item count can't be zero or less than that")


def coupon_validation(date):
    if date <= timezone.now().date():
        raise ValidationError("Invalid date of expiry")
