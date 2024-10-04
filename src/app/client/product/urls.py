from django.urls import path

from src.app.client.product.views import ProductDetailView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/<int:pk>', ProductDetailView.as_view())
]