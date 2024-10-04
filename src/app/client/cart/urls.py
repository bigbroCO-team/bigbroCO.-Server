from django.urls import path

from src.app.client.cart.views import CartView

urlpatterns = [
    path('', CartView.as_view())
]