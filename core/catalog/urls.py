from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('product_detail/<int:product_id>', views.product_detail_view, name='product_detail'),
    path('categories/', views.category_view, name='categories')
    ]
