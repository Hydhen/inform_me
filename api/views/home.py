from django.http import JsonResponse
from django.shortcuts import render

def Home(request):
    data = "Bienvenue sur Home"
    return JsonResponse(data, safe=False)
