# dashboard/urls.py
"""
URL Configuration for the Dashboard app in the 'monitor' Django project.

This module defines the URL patterns for the Dashboard application. 
It serves as a routing guide for incoming requests 
to the appropriate views within the Dashboard app.

URL Patterns:
- 'pie_chart/': Routes requests to the 'pie_chart' view 
for displaying pie chart visualizations.
- 'home/': Routes requests to the 'home' view, 
which is likely the main landing page of the Dashboard app.
- Other URL patterns can be added here as needed to route to additional views.

The 'path' function is used to define each URL pattern, 
with the route pattern as the first argument,
the view function as the second argument, and an optional 'name' argument for URL naming.
"""
from django.urls import path
from .views import pie_chart,  home


urlpatterns = [
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('home/', home, name='home' ),
    # autres patterns d'URL ici
]
