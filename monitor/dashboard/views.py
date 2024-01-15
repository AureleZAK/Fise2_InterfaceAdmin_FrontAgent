# Create your views here.
# dashboard/views.py
from django.http import HttpResponse


from django.shortcuts import render
from .models import ServerData
import plotly.express as px
import pandas as pd
import requests


def dashboard(request):
    data_points = ServerData.objects.all()  # Récupérez les données depuis la base de données
    return render(request, 'dashboard/dashboard.html', {'data_points': data_points})

def staticinfo(request):
    return render(request, 'dashboard/staticinfo.html')
def home(request):
    return render(request, 'dashboard/home.html')
def my_view(request):
    # votre logique de vue ici
    return HttpResponse("Hello, this is my view!")
# views.py

# views.py



def pie_chart(request):
    # Fake values for the pie chart (replace with your own data)
    #api_url = "http://localhost:8081/metrics/v1/log"
    api_url = ("http://lancelot.telecomste.net:8080/metrics/v1/log")

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        api_data = response.json()
        labels = [200, 404]
        values = [api_data['succeed'], api_data['failed']]
        # Create a Pandas DataFrame
        data = {'labels': labels, 'values': values}
        df = pd.DataFrame(data)

        # Create the pie chart with Plotly Express
        fig = px.pie(df, names='labels', values='values', title='Pie Chart')

        # Convert the chart to HTML
        graph_html = fig.to_html(full_html=False)

        # Render the page with the chart
        return render(request, 'dashboard/pie_chart.html', {'graph_html': graph_html, 'api_data': api_data})
    except requests.RequestException as e:
        # Print the exception to the console for debugging
        print(f"Error in get_api_data: {str(e)}")
        return HttpResponse(f"Erreur de requête: {str(e)}")

# Ajoutez cette fonction à views.py
from django.http import JsonResponse

def ram_data(request):
    api_url = "http://lancelot.telecomste.net:8080/metrics/v1/ram"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        ram_data = response.json()

        return JsonResponse(ram_data)  # Renvoyer les données en tant que réponse JSON
    except requests.RequestException as e:
        print(f"Error in ram_data: {str(e)}")
        return JsonResponse({'error': f"Erreur de requête: {str(e)}"})  # Renvoyer une réponse JSON avec l'erreur


from django.shortcuts import render

def Dym_metrics(request):
    # Logique de la vue ram_chart
    return render(request, 'dashboard/Dym_metrics.html')  # Assurez-vous que le chemin du modèle est correct


def cpu_data(request):
    api_url = "http://lancelot.telecomste.net:8080/metrics/v1/cpu/avg-load"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        cpu_data = response.json()

        return JsonResponse({'load': cpu_data['avgLoad'][0]})  # Renvoyer la première valeur comme exemple
    except requests.RequestException as e:
        print(f"Error in cpu_data: {str(e)}")
        return JsonResponse({'error': f"Erreur de requête: {str(e)}"})  # Renvoyer une réponse JSON avec l'erreur

def disk_data(request):
    api_url = "http://lancelot.telecomste.net:8080/metrics/v1/disk/"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        disk_data = response.json()

        return JsonResponse(disk_data)
    except requests.RequestException as e:
        print(f"Error in disk_data: {str(e)}")
        return JsonResponse({'error': f"Erreur de requête: {str(e)}"})

def top_processes_data(request):
    api_url = "http://lancelot.telecomste.net:8080/metrics/v1/processes"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        top_processes_data = response.json()
        
        return JsonResponse(top_processes_data)
    except requests.RequestException as e:
        print(f"Error in disk_data: {str(e)}")
        return JsonResponse({'error': f"Erreur de requête: {str(e)}"})