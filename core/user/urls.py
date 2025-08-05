from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('verify-login/', views.verify_login_otp_view, name='verify_login_otp'),
    path('resend-login/', views.resend_login_otp_view, name='resend_login_otp'),
    path('logout/', views.logout_view, name='logout'),
    ]

