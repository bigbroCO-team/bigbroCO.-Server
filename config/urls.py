from django.urls import path, include
from django.contrib import admin

from src.app.product.views import ProductAdminView, UploadView

urlpatterns = [

    path('auth', include('src.app.user.urls')),
    path('address', include('src.app.address.urls')),
    path('cart', include('src.app.cart.urls')),
    path('product', include('src.app.product.urls')),
    path('order', include('src.app.order.urls')),

    path('admin/site/', admin.site.urls),
    path('admin/upload', UploadView.as_view()),
    path('admin/product', ProductAdminView.as_view(), name='admin-product'),
    path('admin/product/<int:id>', ProductAdminView.as_view(), name='admin-product'),
]
