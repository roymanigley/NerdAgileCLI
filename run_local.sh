#!/bin/bash

export APP_PROD_ENV='FALSE'
source .env/bin/activate
# python ./manage.py runserver
gunicorn nerd_agile_cli_project.wsgi:application