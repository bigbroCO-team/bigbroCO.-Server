from django.urls import path
from .views import ProductView, CategoryView


urlpatterns = [
    path('', ProductView.as_view()),
    path('<pk:int>/', ProductView.as_view()),

    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryView.as_view()),
]
