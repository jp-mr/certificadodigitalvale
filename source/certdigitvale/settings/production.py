from django.conf import settings

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

    ## Definições para email    
    EMAIL_HOST = 'smtp.mailgun.org'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'postmaster@sandbox9db2e2b439b9427691c56627c732d4f9.mailgun.org'
    EMAIL_HOST_PASSWORD = '6105567ad1c5d6ba793664903dbc7f39'
    EMAIL_USE_TLS = True
    EMAIL_DESTINY = False




    STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static')

    MEDIA_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static', 'media')
