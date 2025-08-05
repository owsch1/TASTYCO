from django.db import models
from django.conf import settings
from catalog.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('processing', 'В обработке'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен'),
        ]

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='orders',
            verbose_name='Пользователь'
            )

    created_at = models.DateTimeField(
            auto_now_add=True,
            verbose_name='Дата создания'
            )

    updated_at = models.DateTimeField(
            auto_now=True,
            verbose_name='Дата обновления'
            )

    status = models.CharField(
            max_length=20,
            choices=STATUS_CHOICES,
            default='pending',
            verbose_name='Статус заказа'
            )

    total_price = models.DecimalField(
            max_digits=10,
            decimal_places=2,
            verbose_name='Итоговая цена'
            )

    def __str__(self):
        return f'Заказ #{self.id} пользователя {self.user.email}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(
            Order,
            on_delete=models.CASCADE,
            related_name='items',
            verbose_name='Заказ'
            )

    product = models.ForeignKey(
            Product,
            on_delete=models.PROTECT,
            verbose_name='Продукт'
            )

    quantity = models.PositiveIntegerField(
            default=1,
            verbose_name='Количество'
            )

    price_per_item = models.DecimalField(
            max_digits=10,
            decimal_places=2,
            verbose_name='Цена за единицу'
            )

    def __str__(self):
        return f'{self.product.name} в заказе #{self.order.id}'

    def get_total_price(self):
        return str(self.quantity * self.price_per_item)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

