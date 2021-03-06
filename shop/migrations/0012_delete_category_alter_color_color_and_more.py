# Generated by Django 4.0.5 on 2022-07-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_category_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(max_length=15, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, to='shop.color', verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img1',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Изображение 1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Изображение 3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img4',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Изображение 4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img5',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Изображение 5'),
        ),
        migrations.AlterField(
            model_name='product',
            name='information',
            field=models.TextField(blank=True, verbose_name='Характеристики'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='oldprice',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Старая цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ratingpeople',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Количество отзывов'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_desc',
            field=models.TextField(blank=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, to='shop.size', verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AlterField(
            model_name='size',
            name='universal',
            field=models.CharField(max_length=10, verbose_name='Международная система'),
        ),
    ]
