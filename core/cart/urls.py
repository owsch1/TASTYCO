from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('subtract/<int:product_id>/', views.cart_subtract, name='cart_subtract'),
    path('delete/<int:product_id>/', views.cart_delete, name='cart_delete'),
    path('clear/', views.cart_clear, name='cart_clear'),
    ]
