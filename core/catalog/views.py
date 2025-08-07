from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q  #
from django.core.paginator import Paginator


def index_view(request):
    products = Product.objects.all()
    categories = Category.objects.filter(parent=None)

    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'catalog/index.html',
        context={
            'products': page_obj,  # ⬅️ paginierte Produkte
            'categories': categories,
            'is_paginated': page_obj.has_other_pages(),
            'page_obj': page_obj,
            'paginator': paginator,
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
def about_view(request):
    return render(request, 'catalog/about.html')

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(
        request,
        'catalog/product_detail.html',
        context={'product': product},
    )
