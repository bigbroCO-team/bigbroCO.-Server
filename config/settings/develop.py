from .base import *

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('SERVER')]

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
            "class": "utils.discord.DiscordWebhookHandler",
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
