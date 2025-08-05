from django.db import models
from django.conf import settings
from orders.models import Order


class Transaction(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Ожидается'),
        ('success', 'Успешно'),
        ('failed', 'Неудача'),
        ('refunded', 'Возврат'),
    ]

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            verbose_name='Пользователь'
            )

    order = models.OneToOneField(
            Order,
            on_delete=models.CASCADE,
            verbose_name='Заказ',
            related_name='transaction'
            )

    amount = models.DecimalField(
            max_digits=10,
            decimal_places=2,
            verbose_name='Сумма оплаты'
            )

    status = models.CharField(
            max_length=20,
            choices=PAYMENT_STATUS_CHOICES,
            default='pending',
            verbose_name='Статус оплаты'
            )

    transaction_id = models.CharField(
            max_length=255,
            blank=True,
            null=True,
            verbose_name='ID транзакции (от платежной системы)'
            )

    created_at = models.DateTimeField(
            auto_now_add=True,
            verbose_name='Создано'
            )

    updated_at = models.DateTimeField(
            auto_now=True,
            verbose_name='Обновлено'
            )

    def __str__(self):
        return f'Транзакция #{self.pk} — {self.status}'

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

