from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import Transaction
from orders.models import Order


@login_required
def manual_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    payment, created = Transaction.objects.get_or_create(
            order=order,
            defaults={
                'amount': order.total_price,
                'user': request.user
                }
            )

    if request.method == 'POST':
        payment.is_confirmed = True
        payment.save()

        order.is_paid = True
        order.save()
        return redirect('order_detail', order_id=order.id)

    return render(
            request,
            'payments/manual_payment.html',
            context={
                'order': order,
                'payment': payment
                }
            )
 
