from django.contrib import admin

from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'size', 'order_status', 'quantity']
    list_filter = ['quantity', 'created_at', 'order_status', 'size']