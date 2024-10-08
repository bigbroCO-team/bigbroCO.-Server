from django.urls import path

from src.app.client.product.views import ProductDetailView, ProductListView


urlpatterns = [
    path(
        '',
        ProductListView.as_view(),
        name='product-list'
    ),
    path(
        '<int:pk>/',
        ProductDetailView.as_view(),
        name='product-detail'
    )
]
