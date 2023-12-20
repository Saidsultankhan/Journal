from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('src.apps.jounal.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

] + urls
