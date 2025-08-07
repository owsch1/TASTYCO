from django.urls import path
from . import views


urlpatterns = [
    path('checkout', views.checkout_view, name='checkout'),
    path('', views.order_list_view, name='order_list'),
    path('detail/<int:order_id>', views.order_detail_view, name='order_detail'),
    path('admin_order_list/', views.admin_order_list_view, name='admin_order_list'),
]

