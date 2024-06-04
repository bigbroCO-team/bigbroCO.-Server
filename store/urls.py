from django.urls import path
from .views import CartView


urlpatterns = [
    path('store/cart/', CartView.as_view()),
    path('store/cart/<str:pk>/', CartView.as_view()),
]