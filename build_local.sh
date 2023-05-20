#!/bin/bash

export APP_PROD='FALSE'
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py migrate  --run-syncdb
export DJANGO_SUPERUSER_USERNAME='admin'
export DJANGO_SUPERUSER_PASSWORD='admin'
export DJANGO_SUPERUSER_EMAIL='admin@admin.local'
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser --noinput || echo 'Superuser already exists'