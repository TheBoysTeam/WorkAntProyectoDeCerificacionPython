from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def login(request):
    return render(request,"login.html",{'llaveALaVerga':"ValorALaVerga"})
def registerempleado(request):
    return render(request,"registerempleado.html",{'llaveALaVerga0':"ValorALaVerga0"})    
def registerempresa(request):
	return render(request,"registerempresa.html",{'llaveALaVerga1':"ValorALaVerga1"})
def recordsempleado(request):
	return render(request,"recordsempleado.html",{'llaveALaVerga2':"ValorALaVerga2"})
def homeempleador(request):
	return render(request,"homeempleador.html",{'llaveALaVerga3':"ValorALaVerga3"})
def descripcionempleado(request):
	return render(request,"descripcionempleado.html",{'llaveALaVerga4':"ValorALaVerga4"})
def forgotpassword(request):
	return render(request,"forgotpassword.html",{'llaveALaVerga5':"ValorALaVerga5"})
def e404(request):
	return render(request,"404.html",{'llaveALaVerga6':"ValorALaVerga6"})
def homeempleado(request):
	return render(request,"homeempleado.html",{'llaveALaVerga7':"ValorALaVerga7"})