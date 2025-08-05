from django import forms
from .models import CartItem

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs=
                {'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs=
                {'class': 'form-control', 'min': 1}),
        }

