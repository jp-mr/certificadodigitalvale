#!/bin/bash

export DJANGO_SETTINGS_MODULE='certdigitvale.settings'

# Activate the virtual environment
source $VIRTUAL_ENV/bin/activate

cd $SOURCE_DIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn certdigitvale.wsgi:application \
        --workers 3 \
        -b 127.0.0.1:9000\
        --log-level=debug \
        --log-file=-
