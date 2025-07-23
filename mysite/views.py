from django.http import HttpResponse

def lobby_view(request):
    return HttpResponse("Benvenuto nella lobby! Qui puoi navigare tra le varie sezioni del sito.")

