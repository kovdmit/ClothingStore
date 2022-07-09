from django.db import models
from django.urls import reverse


class Photo(models.Model):
    img1 = models.ImageField(upload_to='photo/%Y/%m/%d/')
    img2 = models.ImageField(upload_to='photo/%Y/%m/%d/')
    img3 = models.ImageField(upload_to='photo/%Y/%m/%d/')
    img4 = models.ImageField(upload_to='photo/%Y/%m/%d/')
    img5 = models.ImageField(upload_to='photo/%Y/%m/%d/')




class Category(models.Model):
    name = models.CharField(max_length=100)


class Size(models.Model):
    universal = models.CharField(max_length=10)


class Color(models.Model):
    color = models.CharField(max_length=15)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    photo = models.ForeignKey(Photo, on_delete=models.PROTECT)
    short_desc = models.TextField()
    description = models.TextField()
    information = models.TextField()
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    rating = models.PositiveSmallIntegerField()
    views = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
