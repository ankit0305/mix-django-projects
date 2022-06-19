from django.urls import path

# Import the home view
from .views import home_view, redirect_url_view

name = "shortner"

urlpatterns = [
    # Home view
    path('/', home_view, name="urlshortner"),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]
