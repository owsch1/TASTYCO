from django.shortcuts import render
from .models import Product, Category


def index_view(request):
    products = Product.objects.all()
    return render(
            request,
            'catalog/index.html',
            context={'products':products},
        )

def product_detail_view(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(
            request,
            'catalog/product_detail.html',
            context={'product':product},
        )

def category_view(request):
    categories = Category.objects.filter(parent=None)
    return render(
        request,
        'catalog/category.html',
        context={'categories': categories},
    )

