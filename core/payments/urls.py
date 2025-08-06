from django.urls import path
from . import views

urlpatterns = [
    path('pay/<int:order_id>/', views.manual_payment, name='payment'),
]
