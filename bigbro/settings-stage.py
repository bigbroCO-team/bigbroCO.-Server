import environ

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