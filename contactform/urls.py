from django.urls import path

from contactform.views import home_view

urlpatterns = [
     # Home view
    path('/', home_view, name="contactform"),
]
