from django.urls import path

from src.app.order.views import OrderListView, TossPaymentsView

urlpatterns = [
    path('', OrderListView.as_view()),
    path('/payments', TossPaymentsView.as_view())
]