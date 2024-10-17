import boto3
import environ

from .settings import *

environ.Env.read_env(os.path.join(BASE_DIR, '.env.prod'))

DEBUG = False

ALLOWED_HOSTS = [
    'api.bigbro.company'
]

# RDS
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('AWS_RDS_DATABASE'),
#         'USER': os.getenv('AWS_RDS_USER_ID'),
#         'PASSWORD': os.getenv('AWS_RDS_PW'),
#         'HOST': os.getenv('AWS_RDS_HOST'),
#         'PORT': os.getenv('AWS_RDS_PORT'),
#     }
# }

# AWS
AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_LOG_GROUP_NAME = os.environ.get('AWS_LOG_GROUP_NAME')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_FILE_OVERWRITE = False

# Cloudwatch
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

# S3
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}

ADMIN_MEDIA_PREFIX = 'admin/'
STATIC_URL = 'static/'
IMAGE_ROOT = 'image/'

