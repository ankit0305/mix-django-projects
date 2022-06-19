from django.urls import path
#from django.urls import re_path as url
from . import views
#from .views import delete_city_view

urlpatterns = [
    path('',views.index, name='weatherinfo'),
#    url('delete', delete_city_view, name='delete'),
]