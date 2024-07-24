from django.urls import path

from cart.views import CartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('<int:id>/', CartView.as_view())
]