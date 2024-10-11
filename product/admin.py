from django.contrib import admin

from product.models import Product, Option, Image

# Register your models here.
admin.site.register(Product)
admin.site.register(Option)
admin.site.register(Image)