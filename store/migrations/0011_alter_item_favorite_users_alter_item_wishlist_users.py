# Generated by Django 4.1.1 on 2022-10-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_delete_customers_customer_user'),
        ('store', '0010_remove_like_product_remove_like_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='favorite_users',
            field=models.ManyToManyField(blank=True, related_name='item_favorite', to='base.customer'),
        ),
        migrations.AlterField(
            model_name='item',
            name='wishlist_users',
            field=models.ManyToManyField(blank=True, related_name='item_wishlist', to='base.customer'),
        ),
    ]