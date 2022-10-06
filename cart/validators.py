from django.core.exceptions import ValidationError


def item_count_ge_zero(count):
    if count <= 0:
        raise ValidationError("Item count can't be zero or less than that")
