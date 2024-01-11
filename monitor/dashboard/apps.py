"""Module configuration for the Dashboard app in the 'monitor' Django project.

This module defines the application-specific configuration for the Dashboard app within the Django 
project.
It is used for app-related settings such as the application's name, default model field definitions,
and other app-specific configurations.
"""
from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """
    Application configuration for the Dashboard app in the 'monitor' Django project.

    Inherits from Django's AppConfig class and sets specific settings for the Dashboard app.
    - 'name': The name of the application used in Django.
    - 'default_auto_field': Specifies the default type of auto-increment field for models 
    in the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
