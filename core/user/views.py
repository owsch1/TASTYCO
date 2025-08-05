from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import login, logout
import random
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from user.models import CustomUser, EmailOTP
from user.forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from cart.models import Cart


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

            cart = Cart.objects.create(
                    user=user
                    )

            return redirect('index')
    else:
        form = RegisterForm()

    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                messages.error(request, 'Пользователь с таким email не найден.')
                return redirect('login')

            code = f"{random.randint(100000, 999999)}"
            EmailOTP.objects.create(user=user, code=code)

            send_mail(
                subject='Код входа в систему',
                message=f'Ваш код входа: {code}',
                from_email='esen.belov@mail.ru',
                recipient_list=[email],
                fail_silently=False,
            )

            request.session['login_email'] = email
            messages.info(request, 'Код отправлен на email')
            return redirect('verify_login_otp')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})


def verify_login_otp_view(request):
    email = request.session.get('login_email')
    if not email:
        messages.error(request, 'Сначала введите email.')
        return redirect('login')

    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        messages.error(request, 'Пользователь не найден.')
        return redirect('login')

    if request.method == 'POST':
        code_input = request.POST.get('code')
        try:
            otp = EmailOTP.objects.get(user=user, code=code_input)
        except EmailOTP.DoesNotExist:
            messages.error(request, 'Неверный код.')
            return redirect('verify_login_otp')

        if otp.is_expired():
            otp.delete()
            messages.warning(request, 'Код истек. Запросите новый.')
            return redirect('verify_login_otp')

        login(request, user)
        EmailOTP.objects.filter(user=user).delete()
        del request.session['login_email']
        messages.success(request, 'Вы успешно вошли в систему.')
        return redirect('index')

    return render(request, 'user/verify_login_otp.html', {'email': email})


def resend_login_otp_view(request):
    email = request.session.get('login_email')
    if not email:
        messages.error(request, 'Сначала введите email.')
        return redirect('login')

    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        messages.error(request, 'Пользователь не найден.')
        return redirect('login')

    EmailOTP.objects.filter(user=user).delete()

    code = f"{random.randint(100000, 999999)}"
    EmailOTP.objects.create(user=user, code=code)

    send_mail(
        subject='Новый код входа',
        message=f'Ваш новый код: {code}',
        from_email='esen.belov@mail.ru',
        recipient_list=[email],
        fail_silently=False,
    )

    messages.success(request, 'Новый код отправлен на email.')
    return redirect('verify_login_otp')

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

