from django.shortcuts import render


def index(request):
    context = {'index': True}
    return render(request, 'shop/shop_index.html', context)


def contact(request):
    return render(request, 'shop/contact.html')
