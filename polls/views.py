# polls/views.py
from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


# Create your views here.

def index(request):

    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'lastest_question_list': lastest_question_list,
    }

    return render(request, 'polls/index.html', context)



    # return HttpResponse("Ciao, Valen! La tua app Django 'polls' funziona!")
