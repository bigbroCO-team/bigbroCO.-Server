from django.urls import path

from thirdparty.s3.views import UploadView

urlpatterns = [
    path('', UploadView.as_view()),
]