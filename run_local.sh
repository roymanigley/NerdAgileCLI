#!/bin/bash

export APP_PROD='FALSE'
source .env/bin/activate
python ./manage.py runserver