from django.urls import path, include

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('catalog/', catalog, name='catalog'),
    path('detail/<int:pk>/', detail, name='detail'),
]

