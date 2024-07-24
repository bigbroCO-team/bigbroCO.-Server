from .base import *

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('SERVER')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT")
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379"

    }
}


# Logging
boto3_client = boto3.client('logs', region_name=os.environ.get('AWS_REGION_NAME'))

AWS_LOG_GROUP = os.environ.get('AWS_LOG_GROUP')
AWS_LOG_STREAM = os.environ.get('AWS_LOG_STREAM')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'aws': {
            'format': u"%(asctime)s [%(levelname)-8s] %(funcName)s - %(message)s [%(pathname)s:%(lineno)d]",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'net_aws': {
            'format': u"%(asctime)s [%(levelname)-8s] %(funcName)s - %(message)s [%(pathname)s:%(lineno)d]",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        }
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'watchtower.CloudWatchLogHandler',
            'boto3_client': boto3_client,
            'log_group': AWS_LOG_GROUP,
            'stream_name': AWS_LOG_STREAM,
            'formatter': 'aws',
            'use_queues': True,
        },
        'network': {
            'level': 'INFO',
            'class': 'watchtower.CloudWatchLogHandler',
            'boto3_client': boto3_client,
            'log_group': AWS_LOG_GROUP,
            'stream_name': AWS_LOG_STREAM,
            'formatter': 'net_aws',
            'use_queues': True,
        }
    },
    'loggers': {
        'default-logger': {
            'level': 'INFO',
            'handlers': ['default'],
            'propagate': False,
        },
        'network-logger': {
            'level': 'DEBUG',
            'handlers': ['network'],
            'propagate': False,
        }
    },
}

log = logging.getLogger('default-logger')
net_log = logging.getLogger('network-logger')
