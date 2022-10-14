# Generated by Django 4.1.1 on 2022-09-29 17:54

from django.db import migrations, models
import store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_item_is_bookmarked'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ratings',
            field=models.FloatField(null=True, validators=[store.validators.check_valid_ratings]),
        ),
    ]
