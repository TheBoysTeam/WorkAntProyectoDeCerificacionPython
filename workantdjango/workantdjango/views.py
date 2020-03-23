from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def login(request):
    return render(request,"login.html",{'llaveALaVerga':"ValorALaVerga"})
def registerempresa(request):
	return render(request,"registerempresa.html",{'llaveALaVerga1':"ValorALaVerga1"})