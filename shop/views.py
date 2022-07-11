from django.shortcuts import render

from shop.models import Product


def index(request):
    context = {'index': True}
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
        round(rating1) * '<small class="fas fa-star"></small>' + # Вывод заполненных звёзд
        rating05 +                                              # Вывод 1/2 заполненных звёзд
        round(rating0) * '<small class="far fa-star"></small>' # Вывод незаполненных звёзд
    )
    # Вывод звёздочек рейтинга конец

    context = {
        'product': Product.objects.get(pk=pk),
        'rating': rating
    }
    return render(request, 'shop/detail.html', context)
