from django.conf import settings

from certdigitvale.keywords import keys

import os


# if os.environ['USER'] == 'jelastic':
if 'OPENSHIFT_CLOUD_DOMAIN' in os.environ:

    DEBUG = False

    SECRET_KEY = os.environ['SECRET_TOKEN']

    ALLOWED_HOSTS = [os.environ['ALLOWED_HOST_URL']]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('MYSQL_DB_NAME'),
            'USER': os.getenv('MYSQL_DB_USERNAME'),
            'PASSWORD': os.getenv('MYSQL_DB_PASSWORD'),
            'HOST': os.getenv('MYSQL_DB_HOST'),
            'PORT': os.getenv('MYSQL_DB_PORT'),
        }
    }

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': os.environ['MEMCACHED_LOCATION'],
        }
    }

    KW = keys()

    ## Definições para email    
    EMAIL_HOST = 'smtp.mailgun.org'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = KW[1]
    EMAIL_HOST_PASSWORD = KW[2]
    EMAIL_USE_TLS = True
    EMAIL_DESTINY = False

    STATIC_ROOT = os.path.join(os.environ['REPO_DIR'], 'static')

    MEDIA_URL = '/static/media/'
    MEDIA_ROOT = os.path.join(os.environ['REPO_DIR'], 'static', 'media')
