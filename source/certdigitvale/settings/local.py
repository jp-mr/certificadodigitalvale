# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party apps
    'crispy_forms',
    #project apps
    'core',
]

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'certdigit',
#        'USER': 'testdjango',
#        'PASSWORD': 'senha123',
#        'HOST': 'localhost',
#        'PORT': 5432,
#    }
#}

# Para testar localmente o envio de email rode em outra 
# instância do terminal o comando:
# $python -m smtpd -n -c DebuggingServer localhost:1025

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = 'test@domain.com'
EMAIL_HOST_PASSWORD = None
EMAIL_DESTINY = False

#Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'
