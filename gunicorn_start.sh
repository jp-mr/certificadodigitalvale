#!/bin/bash

export DJANGO_SETTINGS_MODULE='certdigitvale.settings'

# Activate the virtual environment
source /home/certdigitalvale/venv/bin/activate

cd /home/certdigitalvale/app/certificadodigitalvale/source/

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn -c ../gunicorn_config.py certdigitvale.wsgi:application 
