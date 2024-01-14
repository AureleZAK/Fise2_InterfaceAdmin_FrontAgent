# dashboard/urls.py

from django.urls import path
from .views import pie_chart,  home, dashboard,ram_chart,ram_data


urlpatterns = [
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('home/', home, name='home' ),
    path('', dashboard, name='dashboard'),
    path('ram_chart/', ram_chart, name='ram_chart'),
    path('ram_data/', ram_data, name='ram_data'), 
    # autres patterns d'URL ici
]
