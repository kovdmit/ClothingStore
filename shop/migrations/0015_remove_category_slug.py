# Generated by Django 4.0.5 on 2022-07-12 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
