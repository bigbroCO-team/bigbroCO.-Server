from django.urls import path
from .views import LoginView, LogoutView, SignupView, AddressView


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('signup', SignupView.as_view(), name='signup'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('address', AddressView.as_view(), name='address')
]
