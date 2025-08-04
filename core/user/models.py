from django.db import models
import random
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('manager', 'Менеджер'),
        ('client', 'Клиент'),
    ]


class CustomUserManager(BaseUserManager):
    def create_user(
            self, 
            email, 
            password=None, 
            **extra_fields
            ):
        if not email:
            raise ValueError('Email обязателен для регистрации')
        email = self.normalize_email(email)
        user = self.model(
                email=email, 
                **extra_fields
                )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, 
            email, 
            password=None, 
            **extra_fields
            ):

        extra_fields.setdefault(
                'is_staff', 
                True
                )

        extra_fields.setdefault(
                'is_superuser', 
                True
                )

        extra_fields.setdefault(
                'is_active',
                True
                )

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                    'Superuser должен иметь is_staff=True.'
                )

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                    'Superuser должен иметь is_superuser=True.'
                )

        return self.create_user(
                email, 
                password, 
                **extra_fields
                )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(
            max_length=30,
            verbose_name='Имя'
            )

    lastname = models.CharField(
            max_length=30,
            verbose_name='Фамилия'
            )

    email = models.EmailField(
            unique=True, 
            verbose_name='Электронная почта'
            )

    phone = models.CharField(
            max_length=30,
            blank=True, 
            null=True, 
            verbose_name='Телефон'
            )
    role = models.CharField(
            max_length=30,
            choices=ROLE_CHOICES,
            default='client',
            verbose_name='Роль'
            )

    avatar = models.ImageField(
            upload_to='avatars/', 
            blank=True, 
            null=True, 
            verbose_name='Аватар'
            )

    is_verified = models.BooleanField(
            default=False, 
            verbose_name='Подтвержден'
            )

    is_staff = models.BooleanField(
            default=False, 
            verbose_name='Сотрудник'
            )

    is_active = models.BooleanField(
            default=True,
            verbose_name='Активен'
            )

    created_at = models.DateTimeField(
            default=timezone.now, 
            verbose_name='Дата регистрации'
            )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.firstname} {self.lastname} ({self.email})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class EmailOTP(models.Model):
    user = models.ForeignKey(
            CustomUser,
            on_delete=models.CASCADE,
            verbose_name='Пользователь',
            )

    code = models.CharField(
            max_length=6
            )

    created_at = models.DateTimeField(
            auto_now_add=True
            )

    is_used = models.BooleanField(
            default=False
            )

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=3)

    class Meta:
        verbose_name = 'Одноразовый код'
        verbose_name_plural = 'Одноразовый код'

