from .models import Order, OrderItem
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def checkout_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        return redirect('cart')
    order = Order.objects.create(
            user=request.user,
            total_price=cart.get_total_price()
            )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price_per_item=item.product.price,
        )

    cart_items.delete()
    return redirect('order_detail', order_id=order.id)


@login_required
def order_list_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

