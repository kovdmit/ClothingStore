from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100, verbose_name='Наименование категории')
    img = models.ImageField(upload_to='photo/cat/', blank=True, verbose_name='Изображение')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    # def get_absolute_url(self):
    #     return reverse('index', kwargs={'pk': self.pk})


class Size(models.Model):
    universal = models.CharField(max_length=10, verbose_name='Международная система')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.universal


class Color(models.Model):
    color = models.CharField(max_length=15, verbose_name='Цвет')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвет'

    def __str__(self):
        return self.color


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    price = models.PositiveIntegerField(null=True, verbose_name='цена')
    oldprice = models.PositiveIntegerField(blank=True, null=True, verbose_name='Старая цена')
    img1 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Изображение 1')
    img2 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Изображение 2')
    img3 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Изображение 3')
    img4 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Изображение 4')
    img5 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Изображение 5')
    short_desc = models.TextField(blank=True, verbose_name='Примечание')
    description = models.TextField(blank=True, verbose_name='Описание')
    information = models.TextField(blank=True, verbose_name='Характеристики')
    size = models.ManyToManyField(Size, blank=True, verbose_name='Размер')
    color = models.ManyToManyField(Color, blank=True, verbose_name='Цвет')
    rating = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Рейтинг')
    ratingpeople = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Количество отзывов')
    views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = TreeForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
