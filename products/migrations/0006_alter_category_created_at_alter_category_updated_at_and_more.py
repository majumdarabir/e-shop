# Generated by Django 4.0.2 on 2022-09-17 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
