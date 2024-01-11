# models.py dans votre application "dashboard"
"""Models for the Dashboard app in the 'monitor' Django project.

This module defines the database models for the Dashboard application. 
These models represent the data structure that the Dashboard app will use 
to store and retrieve information from the database.
"""
from django.db import models

class ServerData(models.Model):
    """
    Example model for the Dashboard application.

    This model represents an example entity in the Dashboard app with fields like 'name' 
    and 'description'.
    - 'name': CharField to store the name of the entity.
    - 'description': TextField to store a detailed description.
    """

    # Vos champs de modèle vont ici
    champ1 = models.CharField(max_length=100)
    champ2 = models.IntegerField()
    # Ajoutez plus de champs au besoin

    def __str__(self):
        return f"{self.champ1} - {self.champ2}"
        # Ajustez ceci en fonction de la structure de votre modèle
