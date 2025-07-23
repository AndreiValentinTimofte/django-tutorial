# polls/views.py
from django.http import HttpResponse

def ticketing(request, dataelab:str):
    return HttpResponse(f"classificazione in data {dataelab}")



