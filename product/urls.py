from django.urls import path

from product.views import ProductDetailView, ProductListView


urlpatterns = [
    path(
        '',
        ProductListView.as_view(),
        name='product'
    ),
    path(
        '<int:pk>/',
        ProductDetailView.as_view(),
        name='product-detail'
    )
]
