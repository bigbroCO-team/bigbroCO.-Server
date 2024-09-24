from django.contrib import admin

from src.app.product.models import Product, Image, Option

# Register your models here.
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Option)