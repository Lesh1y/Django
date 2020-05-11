import json
from django.shortcuts import render


# Create your views here.

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
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/catalog.html', content)


def contacts(request):
    with open('mainapp/data.json', 'r', encoding='utf-8') as f:
        products = json.load(f)

    title = 'Контакты'
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/contacts.html', content)


def product1(request):
    with open('mainapp/data.json', 'r', encoding='utf-8') as f:
        products = json.load(f)

    title = 'Продукт'
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/catalog/product_1.html', content)

