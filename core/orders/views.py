from .models import Order, OrderItem
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from user.models import CustomUser


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
    return render(
            request,
            'orders/order_list.html',
            {'orders': orders}
            )


@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(
            Order, id=order_id,
            user=request.user
            )

    return render(
            request,
            'orders/order_detail.html',
            {'order': order}
            )


@login_required
def admin_order_list_view(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return redirect('order_list')
    user_id = request.GET.get('user')
    orders = None
    if user_id:
        selected_user = get_object_or_404(
                CustomUser,
                id=user_id
                )

        orders = Order.objects.filter(user=selected_user)
    users = CustomUser.objects.filter(
            role='client',
            orders__isnull=False
            ).distinct()

    return render(
            request,
            'orders/admin_order_list.html',
            context={
                'orders': orders,
                'users': users, 
                'selected_user': user_id
                    }
            )

