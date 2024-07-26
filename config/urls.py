from django.urls import path, include
from django.contrib import admin

from product.views import ProductAdminView, UploadView

urlpatterns = [

    path('auth', include('user.urls')),
    path('address', include('address.urls')),
    path('cart', include('cart.urls')),
    path('product', include('product.urls')),

    # Todo
    path('admin/site', admin.site.urls),
    path('admin/upload', UploadView.as_view()),
    path('admin/product', ProductAdminView.as_view(), name='admin-product'),
    path('admin/product/<int:id>', ProductAdminView.as_view(), name='admin-product'),


]
