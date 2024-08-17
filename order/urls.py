from django.urls import path

from order.views import OrderListView, TossPaymentsView

urlpatterns = [
    path('', OrderListView.as_view()),
    path('/payments', TossPaymentsView.as_view())
]