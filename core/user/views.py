from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import login, logout as django_logout
import random
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from user.models import CustomUser, EmailOTP
from user.forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password


from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                firstname=firstname,
                lastname=lastname
            )
            return redirect('index')
    else:
        form = RegisterForm()

    return render(request, 'user/register.html', {'form': form})

