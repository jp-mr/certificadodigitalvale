from django.conf import settings

from certdigitvale.keywords import keys

import os


if 'OPENSHIFT_REPO_DIR' in os.environ:

    DEBUG = False

    SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']

    ALLOWED_HOSTS = [os.environ['OPENSHIFT_APP_DNS']]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('OPENSHIFT_APP_NAME'),
            'USER': os.getenv('OPENSHIFT_POSTGRESQL_DB_USERNAME'),
            'PASSWORD': os.getenv('OPENSHIFT_POSTGRESQL_DB_PASSWORD'),
            'HOST': os.getenv('OPENSHIFT_POSTGRESQL_DB_HOST'),
            'PORT': os.getenv('OPENSHIFT_POSTGRESQL_DB_PORT'),
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

    STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static')

    MEDIA_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static', 'media')
