from .base import *

SECRET_KEY = os.urandom(32).hex()

DEBUG = True

ALLOWED_HOSTS = ['*']