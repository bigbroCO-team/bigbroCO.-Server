from django.urls import path
from .views import ProductView, CategoryView, SizeView

urlpatterns = [
    path('', ProductView.as_view()),
    path('<int:pk>/', ProductView.as_view()),

    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryView.as_view()),

    path('size/', SizeView.as_view()),
    path('size/<int:pk>/', SizeView.as_view()),
]
