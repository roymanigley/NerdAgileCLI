from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.views.static import serve

from nerd_agile_cli_rest_api.views import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    # path('static/', serve, {'document_root': settings.STATIC_ROOT, })
]
# only works when DEBUG=True
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = TemplateView.as_view(template_name='errors/404.html')
