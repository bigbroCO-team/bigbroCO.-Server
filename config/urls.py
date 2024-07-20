from django.urls import path, include
from django.contrib import admin

from product.views import ProductView, ProductAdminView

urlpatterns = [
    path('dashboard/', admin.site.urls),

    path('auth/', include('user.urls')),
    path('address/', include('address.urls')),
    path('cart/', include('cart.urls')),
    path('product/', include('product.urls')),

    # Todo
    path('admin/upload/', include('thirdparty.s3.urls')),
    path('admin/product/', ProductAdminView.as_view(), name='admin-product'),
    path('admin/product/<int:id>/', ProductAdminView.as_view(), name='admin-product'),
]
