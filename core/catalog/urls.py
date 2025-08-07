from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('category/<int:category_id>/', views.category_view, name='category'),  # <-- neu
    path('about/', views.about_view, name='about'),
]