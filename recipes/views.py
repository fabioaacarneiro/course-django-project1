from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Home</h1>")


def contato(request):
    return HttpResponse("<h1>Contato</h1>")


def sobre(request):
    return HttpResponse("<h1>Sobre</h1>")

