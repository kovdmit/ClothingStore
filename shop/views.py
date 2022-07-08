from django.shortcuts import render


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


def detail(request):
    return render(request, 'shop/detail.html')