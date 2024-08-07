from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("¡Hola, mundo! Este es mi primer proyecto Django.")
