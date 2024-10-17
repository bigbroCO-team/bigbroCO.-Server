import os

import environ
import boto3
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .settings import *
from .urls import urlpatterns


environ.Env.read_env(os.path.join(BASE_DIR, '.env.stage'))

DEBUG = False

ALLOWED_HOSTS += [
    'stage.api.bigbro.company'
]

urlpatterns += [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_LOG_GROUP_NAME = os.environ.get('AWS_LOG_GROUP_NAME')

boto3_logs_client = boto3.client(
    "logs",
    region_name=AWS_REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['watchtower', 'console'],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'watchtower': {
            'class': 'watchtower.CloudWatchLogHandler',
            'boto3_client': boto3_logs_client,
            'log_group_name': AWS_LOG_GROUP_NAME,
            'level': 'DEBUG',
        }
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        }
    }
}