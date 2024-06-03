from django.urls import path
from .views import ProductView, CategoryView

urlpatterns = [
    path('', ProductView.as_view()),
    path('category/', CategoryView.as_view()),

    path('<str:pk>/', ProductView.as_view()),
    path('category/<str:pk>/', CategoryView.as_view()),
]
