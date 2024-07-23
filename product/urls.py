from django.urls import path

from product.views import GetProductByIdView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:id>/', GetProductByIdView.as_view()),
]