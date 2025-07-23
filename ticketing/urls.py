# polls/urls.py
from django.urls import path
from . import views

app_name = "ticketing" # Questo è per il namespacing degli URL, utile in progetti più grandi
urlpatterns = [
    path("ticketing", views.ticketing, name="ticketing"), # Questo mappa l'URL vuoto (es. /polls/) alla vista 'index'
]