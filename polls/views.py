# polls/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Ciao, Valen! La tua app Django 'polls' è in esecuzione correttamente.")
