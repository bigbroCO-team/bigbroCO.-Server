from .base import *
import logging.config


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
