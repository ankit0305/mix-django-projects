from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),  # new
]