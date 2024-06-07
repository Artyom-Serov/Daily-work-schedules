"""
Main URL configuration for "Daily work schedules" project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('schedules.urls')),
    path("users/", include('users.urls'))
]
