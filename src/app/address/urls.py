from django.urls import path

from .views import AddressView


urlpatterns = [
    path('', AddressView.as_view()),
    path('/<int:id>', AddressView.as_view())
]
