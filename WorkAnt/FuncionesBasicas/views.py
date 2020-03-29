from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

class Persona(object):
	def __init__(self,usuario,contraseña):
		self.usuario = usuario
		self.contraseña = contraseña

def login(request):
    p1 = Persona("","")
    return render(request, "login.html", {'nombrepersona': p1.usuario, 'contraseña': p1.contraseña})

class Empleado(object):
    def __init__(self, nombre):
        self.nombre = nombre
        #, apellido, usuario, contraseña, contraseña2, email, celular, genero, fecha
        #self.apellido = apellido
        #self.usuario = usuario
        #self.contraseña = contraseña
        #self.contraseña2 = contraseña2
        #self.email = email
        #self.celular = celular
        #self.genero = genero
        #self.fecha = fecha

def registerempleado(request):
	#em = Empleado("1")
    return render(request, "registerempleado.html", {'nombre': "em.nombre"})

def registerempresa(request):
    return render(request, "registerempresa.html", {'llaveALaVerga1': "ValorALaVerga1"})


def recordsempleado(request):
    return render(request, "recordsempleado.html", {'llaveALaVerga2': "ValorALaVerga2"})


def homeempleador(request):
    return render(request, "homeempleador.html", {'llaveALaVerga3': "ValorALaVerga3"})


def descripcionempleado(request):
    return render(request, "descripcionempleado.html", {'llaveALaVerga4': "ValorALaVerga4"})


def forgotpassword(request):
    return render(request, "forgotpassword.html", {'llaveALaVerga5': "ValorALaVerga5"})


def e404(request):
    return render(request, "404.html", {'llaveALaVerga6': "ValorALaVerga6"})


def homeempleado(request):
    return render(request, "homeempleado.html", {'llaveALaVerga7': "ValorALaVerga7"})
