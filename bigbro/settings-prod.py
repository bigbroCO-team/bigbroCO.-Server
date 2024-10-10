import environ

from .settings import *


DEBUG = False

environ.Env.read_env(os.path.join(BASE_DIR, '.env.prod'))

ALLOWED_HOSTS += [

]

# RDS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('AWS_RDS_DATABASE'),
        'USER': os.getenv('AWS_RDS_USER_ID'),
        'PASSWORD': os.getenv('AWS_RDS_PW'),
        'HOST': os.getenv('AWS_RDS_HOST'),
        'PORT': os.getenv('AWS_RDS_PORT'),
    }
}
