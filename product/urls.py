from django.urls import path
from .views import ProductView, RatingView

urlpatterns = [
    path('', ProductView.as_view()),
    path('<int:pk>/', ProductView.as_view()),

    path('rating/', RatingView.as_view()),
]
