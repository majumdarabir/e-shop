from django.db import models


class PaymentChoice(models.TextChoices):
    CASH_ON_DELIVERY = 1, "cash on delivery"
    NET_BANKING = 2, 'net banking'
    CREDIT_CARD = 3, 'credit-card'
    DEBIT_CARD = 4, 'debit-card'


class CountryChoices(models.TextChoices):
    UNITED_STATES = 1, "United States"
    INDIA = 2, "India"


class ItemCountChoices(models.TextChoices):
    ONE = 1, "one"
    TWO = 2, "two",
    THREE = 3, "three"
    FOUR = 4, "four"
