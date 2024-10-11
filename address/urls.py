from django.urls import path

from address.views import AddressView, AddressDetailView

urlpatterns = [
    path(
        '',
        AddressView.as_view(),
        name='address',
    ),
    path('<int:pk>/', AddressDetailView.as_view()),
]