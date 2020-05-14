from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('products/', catalog, name='products'),
    path('contact/', contacts, name='contact'),
    path('products/<int:pk>/', products, name='category'),
    path('catalog/products/1/', product1),
]
