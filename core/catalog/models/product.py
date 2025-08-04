from django.db import models


UNIT_CHOICES = [
    ('kg', 'Килограмм'),
    ('g', 'Грамм'),
    ('l', 'Литр'),
    ('pcs', 'Штука'),
]


class Category(models.Model):
    name = models.CharField(
            max_length=100,
            verbose_name='Наименование',
            )

    parent = models.ForeignKey(
            'self',
            on_delete=models.CASCADE,
            null=True,
            blank=True,
            related_name='children'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(
            max_length=255,
            verbose_name='Наименование',
            )

    category = models.ForeignKey(
            Category,
            on_delete=models.CASCADE,
            verbose_name='Категория',
            )

    amount = models.PositiveIntegerField(
            default=0,
            verbose_name='Количество'
            )

    unit = models.CharField(
            max_length=10,
            choices=UNIT_CHOICES,
            verbose_name='Единица измерения'
            )

    price = models.DecimalField(
            max_digits=8,
            decimal_places=2
            )

    description = models.TextField(
            blank=True,
            null=True,
            verbose_name='Описание',
            )

    ingredients = models.TextField(
            verbose_name='Состав',
            )
    
    storage_temp_min = models.DecimalField(
            max_digits=4, 
            decimal_places=1, 
            verbose_name="Минимальная температура хранения °C"
            )

    storage_temp_max = models.DecimalField(
            max_digits=4, 
            decimal_places=1, 
            verbose_name="Максимальная температура хранения °C"
            )

    shelf_life_days = models.PositiveIntegerField(
            verbose_name="Срок хранения в днях"
            )

    calories = models.DecimalField(
            max_digits=6, 
            decimal_places=2, 
            verbose_name="Калорийность (ккал на 100 г)"
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    product = models.ForeignKey(
            Product,
            on_delete=models.CASCADE,
            verbose_name='Продукт',
            )

    image = models.ImageField(
            upload_to='product_images/',
            verbose_name='Изображение',
            )

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

