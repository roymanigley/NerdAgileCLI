import os

API_BASE_URL = os.environ.get('API_BASE_URL') if '' else 'http://127.0.0.1:8000'
API_USERNAME = os.environ.get('API_USERNAME') if '' else 'admin'
API_PASSWORD = os.environ.get('API_PASSWORD') if '' else 'admin'
