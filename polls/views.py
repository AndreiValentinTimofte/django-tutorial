# polls/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Ciao, Valen! La tua app Django 'polls' funziona!")

def ciaomamma(request, saluto:str):
    return HttpResponse(f"Ciao mamma {saluto}")
