bind = "127.0.0.1:9000"
workers = 3
loglevel = "debug"
logfile = "/home/certdigitalvale/app/certificadodigitalvale/logs/gunicorn_supervisor.log"
raw_env = [
    'ENVIRONMENT=production',
    'SECRET_TOKEN=nq#u^m&9gh9bgsq^!_5#s94$3-ynxw1!*4-f2_)e#c5m#!1-=u',
    'ALLOWED_HOST_URL=['127.0.0.1','132.148.72.220'],
    'MEMCACHED_LOCATION=""',
    'DB_NAME=certificadodigitalvale',
    'DB_USERNAME=certdigitvale',
    'DB_PASSWORD=cvm547882',
    'DB_HOST=localhost',
    'DB_PORT=5432',
    'SOURCE_DIR=/home/certdigitalvale/app/certificadodigitalvale/source',
    'REPO_DIR=/home/certdigitalvale/app/certificadodigitalvale/',
    ]
