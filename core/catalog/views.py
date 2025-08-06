from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q


def index_view(request):
    products = Product.objects.all()
    categories = Category.objects.filter(parent=None)
    return render(
        request,
        'catalog/index.html',
        context={
            'products': products,
            'categories': categories,
        },
    )

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(
        request,
        'catalog/product_detail.html',
        context={'product': product},
    )

def category_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    subcategories = category.children.all()

    products = Product.objects.filter(
        Q(category=category) | Q(category__in=subcategories)
    )

    return render(
        request,
        'catalog/category.html',
        context={
            'category': category,
            'products': products,
        },
    )

