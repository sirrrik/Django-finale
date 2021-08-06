from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',include('Posts.urls')),
    path('admin/', admin.site.urls),
    url(r'^Posts/',include('Posts.urls')),
   
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)