from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import PasswordResetForm as DjangoPasswordResetForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(
            widget=forms.PasswordInput,
            label="Пароль"
            )


class PasswordResetForm(DjangoPasswordResetForm):
    email = forms.EmailField(label="Email")


User = get_user_model()


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
                'firstname',
                'lastname',
                'email',
                'phone',
                'avatar'
                )


class OTPForm(forms.Form):
    code = forms.CharField(
            label='Код из почты', 
            max_length=6, 
            widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите 6-значный код'
                })
            )


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = [
                'firstname',
                'lastname',
                'phone',
                'email',
                'password1',
                'password2'
                ]

