# Generated by Django 4.1.1 on 2022-10-01 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_delete_customers_customer_user'),
        ('store', '0008_review_liked_by_review_unliked_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ('-liked_at',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('reviewed_at',)},
        ),
        migrations.RemoveField(
            model_name='item',
            name='is_bookmarked',
        ),
        migrations.RemoveField(
            model_name='item',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='item',
            name='reviews',
        ),
        migrations.AddField(
            model_name='like',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='store.item'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='BookMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_bookmarked', models.BooleanField(default=False)),
                ('bookmarked_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.customer')),
            ],
            options={
                'ordering': ('bookmarked_at',),
            },
        ),
    ]
