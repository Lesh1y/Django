import json
from django.shortcuts import render


# Create your views here.
from .models import ProductCategory, Product
from geekshop import settings


def main(request):
    with open('mainapp/data.json', 'r', encoding='utf-8') as f:
        products = json.load(f)

    title = 'Главная'
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def catalog(request):
    with open('mainapp/data.json', 'r', encoding='utf-8') as f:
        products = json.load(f)

    title = 'Продукты'
    links_menu = ProductCategory.objects.all()
    content = {'title': title, 'links_menu': links_menu, 'products': products}
    return render(request, 'mainapp/catalog.html', content)


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
    }
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/catalog/product_1.html", content)


def contacts(request):
    title = "Контакты"
    locations = [
        {"city": "Москва", "phone": "+7-888-888-8888", "email": "info@geekshop.ru", "address": "В пределах МКАД"},
        {
            "city": "Екатеринбург",
            "phone": "+7-777-777-7777",
            "email": "info_yekaterinburg@geekshop.ru",
            "address": "Близко к центру",
        },
        {
            "city": "Владивосток",
            "phone": "+7-999-999-9999",
            "email": "info_vladivostok@geekshop.ru",
            "address": "Близко к океану",
        },
    ]
    content = {"title": title, "locations": locations}
    return render(request, "mainapp/contacts.html", content)


def product1(request):
    with open('mainapp/data.json', 'r', encoding='utf-8') as f:
        products = json.load(f)

    links_menu = ProductCategory.objects.all()
    title = 'Продукт'
    content = {'title': title, 'links_menu': links_menu, 'products': products}
    return render(request, 'mainapp/catalog/product_1.html', content)

