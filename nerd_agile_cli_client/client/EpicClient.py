from client.generic import GenericClient
from env import API_BASE_URL, API_USERNAME, API_PASSWORD

client = GenericClient(API_BASE_URL, '/api/epic', API_USERNAME, API_PASSWORD)
