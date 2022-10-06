# Generated by Django 4.1.1 on 2022-10-06 16:53

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_item_favorite_users_alter_item_wishlist_users'),
        ('cart', '0003_promocode_alter_cart_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='item',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='store.item'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='valid_till',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
