from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from catalog.models import Product


@login_required
def cart_view(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(
            request,
            'cart/cart.html',
            {'cart': cart}
            )

@login_required
def cart_add(request, product_id):
    cart, created1 = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def cart_subtract(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

@login_required
def cart_delete(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()
    return redirect('cart')

@login_required
def cart_clear(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.items.all().delete()
    return redirect('cart')
