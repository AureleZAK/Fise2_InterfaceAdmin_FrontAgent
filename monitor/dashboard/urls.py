# dashboard/urls.py

from django.urls import path
from .views import pie_chart,  home, dashboard


urlpatterns = [
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('home/', home, name='home' ),
    # autres patterns d'URL ici
]
