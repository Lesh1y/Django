from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    return render(request, 'mainapp/catalog.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def product1(request):
    return render(request, 'mainapp/catalog/product_1.html')
