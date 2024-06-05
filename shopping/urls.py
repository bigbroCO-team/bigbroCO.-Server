from django.urls import path
from .views import CartView, WishListView

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('cart/<str:pk>/', CartView.as_view()),

    path('wish/', WishListView.as_view()),
    path('wish/<str:pk>/', WishListView.as_view()),
]
