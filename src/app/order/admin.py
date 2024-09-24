from django.contrib import admin

from src.app.order.models import Order, OrderItem

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
