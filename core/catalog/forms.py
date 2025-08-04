from django import forms
from .models import Category, Product, ProductImage


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование категории'}),
            'parent': forms.Select(attrs={'class': 'form-select'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'category', 'amount', 'unit', 'price',
            'description', 'ingredients',
            'storage_temp_min', 'storage_temp_max',
            'shelf_life_days', 'calories'
        ]

        widgets = {
            'name': forms.TextInput(attrs=
                {'class': 'form-control', 'placeholder': 'Наименование продукта'}),

            'category': forms.Select(attrs=
                {'class': 'form-select'}),

            'amount': forms.NumberInput(attrs=
                {'class': 'form-control', 'min': 0}),

            'unit': forms.Select(attrs=
                {'class': 'form-select'}),

            'price': forms.NumberInput(attrs=
                {'class': 'form-control', 'step': '0.01', 'min': 0}),

            'description': forms.Textarea(attrs=
                {'class': 'form-control', 'rows': 3, 'placeholder': 'Описание продукта'}),

            'ingredients': forms.Textarea(attrs=
                {'class': 'form-control', 'rows': 3, 'placeholder': 'Состав продукта'}),

            'storage_temp_min': forms.NumberInput(attrs=
                {'class': 'form-control', 'step': '0.1'}),

            'storage_temp_max': forms.NumberInput(attrs=
                {'class': 'form-control', 'step': '0.1'}),

            'shelf_life_days': forms.NumberInput(attrs=
                {'class': 'form-control', 'min': 0}),

            'calories': forms.NumberInput(attrs=
                {'class': 'form-control', 'step': '0.01', 'min': 0}),
        }

