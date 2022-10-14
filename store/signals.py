from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

from products.models import Product
from .models import Item


@receiver([post_save], sender=Product)
def create_item_for_product(sender, instance: Product, created: bool, **kwags):
    if created:
        item_exist = Item.objects.filter(product=instance).first()
        if not item_exist:
            Item.objects.create(product=instance)
