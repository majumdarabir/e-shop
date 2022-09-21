# Generated by Django 4.0.2 on 2022-09-13 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('products', '0003_category_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('payment_options', models.CharField(choices=[('1', 'cash on delivery'), ('2', 'net banking'), ('3', 'credit-card'), ('4', 'debit-card')], max_length=100)),
                ('is_delivered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('had_checkout', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(blank=True, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.customers')),
            ],
        ),
    ]
