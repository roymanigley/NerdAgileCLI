from django.contrib import admin
from django.urls import path
from nerd_agile_cli_rest_api.views import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
