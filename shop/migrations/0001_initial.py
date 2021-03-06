# Generated by Django 4.0.5 on 2022-07-09 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('img2', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('img3', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('img4', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('img5', models.ImageField(upload_to='photo/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universal', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('short_desc', models.TextField()),
                ('description', models.TextField()),
                ('information', models.TextField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('views', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.color')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.photo')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.size')),
            ],
        ),
    ]
