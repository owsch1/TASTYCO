from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'order', 'amount', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['user','order', 'status']

