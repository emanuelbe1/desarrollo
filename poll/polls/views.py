from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("¡Hola!. Este es el indice de encuestas.")
# Create your views
