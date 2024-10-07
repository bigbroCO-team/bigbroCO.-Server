from .base import *

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION = 'ap-northeast-2'
AWS_LOG_GROUP = os.environ.get('AWS_LOG_GROUP')
AWS_LOG_STREAM = os.environ.get('AWS_LOG_STREAM')

boto3_client = boto3.client(
    'logs',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'aws': {
            'format': u"%(asctime)s [%(levelname)-8s] %(funcName)s - %(message)s [%(pathname)s:%(lineno)d]",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        }
    },
    'handlers': {
        'aws-handler': {
            'level': 'INFO',
            'class': 'watchtower.CloudWatchLogHandler',
            'boto3_client': boto3_client,
            'log_group': AWS_LOG_GROUP,
            'stream_name': AWS_LOG_STREAM,
            'formatter': 'aws',
            'use_queues': True,
        },
    },
    'loggers': {
        'aws-logger': {
            'level': 'INFO',
            'handlers': ['aws-handler'],
            'propagate': True,
        }
    }
}

log = logging.getLogger('default-logger')
