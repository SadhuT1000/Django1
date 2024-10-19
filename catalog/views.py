from django.shortcuts import render
from catalog.models import Product, Category
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def info(request, product_id):
    product = Product.objects.get(id=product_id)

    context = {
       'product': product
    }
    return render(request, template_name='catalog/info.html', context=context)


def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, template_name='catalog/all_products.html', context=context)