from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} que tem {idade} anos de idade!</h1>')

def soma(request, vlr1, vlr2):
    return HttpResponse(f'A soma do valor {vlr1} mais o valor {vlr2} tem como resultado: {vlr1+vlr2}')

def subtracao(request, vlr1, vlr2):
    return HttpResponse(f'A soma do valor {vlr1} mais o valor {vlr2} tem como resultado: {vlr1-vlr2}')

def multiplicacao(request, vlr1, vlr2):
    return HttpResponse(f'A soma do valor {vlr1} mais o valor {vlr2} tem como resultado: {vlr1*vlr2}')

def divisao(request, vlr1, vlr2):
    return HttpResponse(f'A soma do valor {vlr1} mais o valor {vlr2} tem como resultado: {vlr1/vlr2}')
