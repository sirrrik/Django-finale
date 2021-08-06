from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static

urlpatterns = [
   url(r'^$',views.index, name='index'),
   url(r'^post/(?P<id>\d+)/$',views.post, name='post'),
   url(r'^about',views.about, name='about'),
   url(r'^contact',views.contact, name='contact'),
   url(r'^register',views.register, name='register'),
    url(r'^extenal',views.extenal ),
 
]

