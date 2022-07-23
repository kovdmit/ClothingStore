# Generated by Django 4.0.5 on 2022-07-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_remove_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование категории'),
        ),
    ]