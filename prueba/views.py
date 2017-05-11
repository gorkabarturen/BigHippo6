from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
	return render(request, 'prueba/index.html')

def SunBurst(request):
        return render(request, 'prueba/pages/SunBurst.html')

def TaxiTracker(request):
	return render(request, 'prueba/pages/TaxiTracker.html')

def heatmap(request):
	return render(request, 'prueba/pages/HeatMap.html')
