from django.db import models
from django.urls import reverse


class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Size(models.Model):
    universal = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.universal


class Color(models.Model):
    color = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвет'

    def __str__(self):
        return self.color


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(null=True)
    img1 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    img2 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    img3 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    img4 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    img5 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    short_desc = models.TextField(blank=True)
    description = models.TextField(blank=True)
    information = models.TextField(blank=True)
    size = models.ManyToManyField(Size, blank=True)
    color = models.ManyToManyField(Color, blank=True)
    rating = models.PositiveSmallIntegerField(blank=True)
    views = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
