from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from CovidML.views import inicio, probabilidadMapa, calcular, nosotros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('mapa/', probabilidadMapa),
    path('calcular/', calcular),
    path('nosotros/', nosotros),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
