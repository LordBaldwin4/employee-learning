import os

from django.core.management.utils import get_random_secret_key

from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SECRET_KEY = os.environ.get('SECRET_KEY') or get_random_secret_key()
