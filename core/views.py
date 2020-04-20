from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} que tem {idade} anos de idade!</h1>')
