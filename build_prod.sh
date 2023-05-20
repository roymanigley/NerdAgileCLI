#!/bin/sh

export APP_PROD='TRUE'
pip install -r requirements.txt
export APP_DATABASE_NAME=$APP_DB_NAME
export APP_DATABASE_USER=$APP_DB_USERNAME
export APP_DATABASE_PASSWORD=$APP_DB_PASSWORD
export APP_DATABASE_PORT=$APP_DB_PORT
export DJANGO_SUPERUSER_USERNAME=$APP_SUPERUSER_NAME
export DJANGO_SUPERUSER_PASSWORD=$APP_DATABASE_PASSWORD
export DJANGO_SUPERUSER_EMAIL=$APP_SUPERUSER_EMAIL
export DJANGO_SECRET_KEY=$APP_SECRET_KEY
python3 manage.py migrate || python manage.py makemigrations
python3 manage.py createsuperuser --noinput
