from django.conf import settings

import os


if os.environ['ENVIRONMENT'] == 'production':

    DEBUG = False

    SECRET_KEY = os.environ['SECRET_TOKEN']

    ALLOWED_HOSTS = [os.environ['ALLOWED_HOST_URL']]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USERNAME'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
        }
    }

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': os.environ['MEMCACHED_LOCATION'],
        }
    }

    ANYMAIL = {
        'MAILGUN_API_KEY': os.environ['MAILGUN_API_KEY'],
        'MAILGUN_SENDER_DOMAIN': os.environ['MAILGUN_SENDER_DOMAIN'],
        }

    EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"

    EMAIL_DESTINY = False

    STATIC_URL = '/public/static/'

    STATIC_ROOT = os.path.join(os.environ['REPO_DIR'], 'public', 'static')

    MEDIA_URL = '/public/media/'

    MEDIA_ROOT = os.path.join(os.environ['REPO_DIR'], 'public', 'media')
