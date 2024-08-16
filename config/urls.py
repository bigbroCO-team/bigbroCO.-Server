from django.urls import path, include
from django.contrib import admin

from product.views import ProductAdminView, UploadView

urlpatterns = [

    path('auth', include('user.urls')),
    path('address', include('address.urls')),
    path('cart', include('cart.urls')),
    path('product', include('product.urls')),
    path('order', include('order.urls')),

    path('manage/site', admin.site.urls),
    path('manage/upload', UploadView.as_view()),
    path('manage/product', ProductAdminView.as_view(), name='admin-product'),
    path('manage/product/<int:id>', ProductAdminView.as_view(), name='admin-product'),
]
