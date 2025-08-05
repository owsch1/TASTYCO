from django.db import models
from django.conf import settings

class Cart(models.Model):
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='cart',
            verbose_name='Пользователь'
            )

    created_at = models.DateTimeField(
            auto_now_add=True
            )

    def __str__(self):
        return f'Корзина пользователя {self.user.email}'

    def get_total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    cart = models.ForeignKey(
            Cart,
            on_delete=models.CASCADE,
            related_name='items',
            verbose_name='Корзина'
            )

    product = models.ForeignKey(
            'catalog.Product',
            on_delete=models.CASCADE,
            verbose_name='Продукт'
            )

    quantity = models.PositiveIntegerField(
            default=1,
            verbose_name='Количество'
            )

    def __str__(self):
        return f'{self.product.name} — {self.quantity} шт.'

    def total_price(self):
        return f'{self.quantity * self.product.price}'

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'

