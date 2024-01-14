# dashboard/urls.py

from django.urls import path
from .views import pie_chart,cpu_data,  home, dashboard,Dym_metrics,ram_data, staticinfo


urlpatterns = [
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('home/', home, name='home'),
    path('', dashboard, name='dashboard'),
    path('Dym_metrics/', Dym_metrics, name='Dym_metrics'),
    path('ram_data/', ram_data, name='ram_data'),
    path('cpu_data/', cpu_data, name='cpu_data'),

    path('staticinfo/', staticinfo, name='staticinfo'),
    # autres patterns d'URL ici
]
