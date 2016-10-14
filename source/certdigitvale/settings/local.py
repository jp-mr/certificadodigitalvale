# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party apps
    'compressor',
    'coverage',
    'crispy_forms',
    #'debug_toolbar',
    'markdown_deux',
    'pagedown',
    #project apps
    'core',
    'cs_modal',
    'info',
    'tabela',
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

INTERNAL_IPS = '127.0.0.1'

COMPRESS_ENABLED = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    )

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
