
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Freebay API')


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/v1/', include('apps.posts.api.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('docs', schema_view),
    path('', schema_view)
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)