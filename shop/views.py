import random

from django.shortcuts import render

from shop.models import Product, Category


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    c = categories.count()
    r = random.randint(0, c)
    if (r + 6) > c:
        r = c - random.randint(6, c)
    context = {
        'index': True,
        'popular_products': products.order_by('views')[:8],
        'new_products': products.order_by('created')[:8],
        'categories': categories,
        'categories_img': categories[r:r+6],
    }
    return render(request, 'shop/shop_index.html', context)


def contact(request):
    return render(request, 'shop/contact.html')


def checkout(request):
    return render(request, 'shop/checkout.html')


def cart(request):
    return render(request, 'shop/cart.html')


def catalog(request):
    return render(request, 'shop/catalog.html')


def detail(request, pk):
    # Вывод звёздочек рейтинга начало
    rating1 = Product.objects.get(pk=pk).rating
    rating0 = 5 - rating1
    rating05 = ''
    if rating1 % 1 >= 0.5:
        rating05 = '<small class="fas fa-star-half-alt"></small>'
        rating1 = rating1 - 1
    rating = (
            round(rating1) * '<small class="fas fa-star"></small>' +  # Вывод заполненных звёзд
            rating05 +  # Вывод 1/2 заполненных звёзд
            round(rating0) * '<small class="far fa-star"></small>'  # Вывод незаполненных звёзд
    )
    # Вывод звёздочек рейтинга конец

    categories = Category.objects.all()

    context = {
        'product': Product.objects.get(pk=pk),
        'rating': rating,
        'categories': categories,
    }
    return render(request, 'shop/detail.html', context)
