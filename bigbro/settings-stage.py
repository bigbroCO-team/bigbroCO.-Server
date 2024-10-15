import os

import environ
import boto3

from .settings import *


environ.Env.read_env(os.path.join(BASE_DIR, '.env.stage'))

DEBUG = False

ALLOWED_HOSTS += [

]

# RDS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('LOCAL_RDS_DATABASE'),
        'USER': os.getenv('LOCAL_RDS_USER_ID'),
        'PASSWORD': os.getenv('LOCAL_RDS_PW'),
        'HOST': os.getenv('LOCAL_RDS_HOST'),
        'PORT': os.getenv('LOCAL_RDS_PORT'),
    }
}

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