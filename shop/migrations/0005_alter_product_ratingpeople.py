# Generated by Django 4.0.5 on 2022-07-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ratingpeople',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
