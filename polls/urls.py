# polls/urls.py
from django.urls import path
from . import views

app_name = "polls" # Questo è per il namespacing degli URL, utile in progetti più grandi
urlpatterns = [
    path("", views.index, name="index"), # Questo mappa l'URL vuoto (es. /polls/) alla vista 'index'
    path("ciaomamma", views.ciaomamma, name="ciaomamma"), # Questo mappa l'URL vuoto (es. /polls/) alla vista 'index'
]