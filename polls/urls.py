# polls/urls.py
from django.urls import path
from . import views

app_name = "polls" # Questo è per il namespacing degli URL, utile in progetti più grandi
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"), # Questo mappa l'URL vuoto (es. /polls/) alla vista 'index'
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]