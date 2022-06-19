from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('', include(('urlshortner.urls', 'home'), namespace='home')),
    path('', include(('contactform.urls', 'home'), namespace='home')),

    # Urls
    path(r'urlshortner', include('urlshortner.urls')),
    path(r'contactform', include('contactform.urls')),
    url(r'weatherinfo', include('weatherinfo.urls')),
    path(r'loginsystem', include('loginsystem.urls')),
]
