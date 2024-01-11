# monitor/urls.py
"""
URL Configuration for the 'monitor' Django project.

This module configures the URLs for the 'monitor' application. It serves as a routing guide, 
directing incoming requests to the appropriate view based on the request URL.

Includes:
- Admin site URLs: Routes for Django's admin interface.
- Dashboard app URLs: Routes for the 'dashboard' application. All requests to the root ('/') 
  are directed to the URLs defined in 'dashboard.urls'.

The 'path' function is used to define each route, where the first argument is the route pattern 
and the second argument is the view or include function to handle the request.

Example:
- Requests to 'http://<domain>/admin/' are routed to Django's admin site.
- Requests to 'http://<domain>/' and its sub-paths are routed to 
the views defined in 'dashboard.urls'.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
]
