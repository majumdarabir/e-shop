from django.db import models


class PaymentChoice(models.TextChoices):
    CASH_ON_DELIVERY = 1, "cash on delivery"
    NET_BANKING = 2, 'net banking'
    CREDIT_CARD = 3, 'credit-card'
    DEBIT_CARD = 4, 'debit-card'
