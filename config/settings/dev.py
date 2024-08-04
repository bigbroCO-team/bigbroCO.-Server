import logging
import logging.config
import os

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

# logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "discord": {
            "level": "WARNING",
            "class": "config.utils.DiscordErrorWebhookHandler.DiscordErrorWebhookHandler",
            "webhook_url": os.environ.get('DISCORD_WEBHOOK_URL'),
        }
    },
    "root": {
        "handlers": ["console", "discord"],
        "level": "ERROR",
    },
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)
