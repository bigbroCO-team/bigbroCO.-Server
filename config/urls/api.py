from django.urls import path, include


urlpatterns = [
    path('auth/', include('user.urls')),
    path('address/', include('address.urls')),
    path('cart/', include('cart.urls')),
    path('upload/', include('thirdparty.s3.urls')),
]
