from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from FuncionesBasicas.models import Empleados, Empleadores
from FuncionesBasicas.llenadorBasico import llenadorTablas
import datetime


def login(request):
    if request.POST.get("usuario", False) and  request.POST.get("contrasena", False):
        if Empleados.objects.filter(nombre=request.POST["usuario"]).filter(codigo=request.POST["contrasena"]):
            return render(request, "homeempleado.html", {'tiempo': "tiempo",'nombre':"nombre", 'apellido':"apellido", 'zona':"zona",'exp':"exp",'anterior':"anterior",'descripcion':"descripcion"})            
        elif Empleadores.objects.filter(nombre=request.POST["usuario"]).filter(codigo=request.POST["contrasena"]):
            return render(request, "homeempleador.html", {'tiempo':" he.tiempo",'nombre':"he.nombre", 'apellido':"he.apellido", 'zona':"he.zona",'exp':"he.exp",'anterior':"he.anterior",'descripcion':"he.descripcion"})
    return render(request, "login.html", {'usuario': "p1.usuario", 'contraseña': "p1.contraseña"})

#------------------------------------------
def registerempleado(request):
    mensaje=""
    bol= (request.POST.get("Username",False) and request.POST.get("Password",False)) and (request.POST.get("RepeatPassword",False) and request.POST.get("Email",False)) and (request.POST.get("NobreDeLaEmpresa",False) and request.POST.get("Celular",False)) and request.POST.get("Genero",False) 
    if bol : 
        if ( request.POST.get("Password",False) == request.POST.get("RepeatPassword",False) ):
            llenador=llenadorTablas
            fecha=datetime.datetime.strptime(request.POST["FechaNac"], "%d%m%Y")
            llenador.llenadorTablasUsuario(request.POST["Username"], request.POST["Password"], fecha, request.POST["Genero"], request.POST["Email"])
            
        else:
            mensaje="Debes repetir el password"
    return render(request, "registerempleado.html", {'mensajePasswordInvalido':mensaje})

#-----------------------------------------
def registerempresa(request):
    mensaje=""
    bol=request.POST.get("Username",False) and request.POST.get("Password",False) and request.POST.get("RepeatPassword",False) and request.POST.get("Email",False) and request.POST.get("NobreDeLaEmpresa",False) and request.POST.get("Celular",False) and request.POST.get("Telefono",False) and request.POST.get("EmailEmp",False)
    if bol:
        if ( request.POST.get("Password",False) == request.POST.get("RepeatPassword",False) ):
            llenador=llenadorTablas
            ob=llenador.llenadorTablasEmpleadores(request.POST["Username"], request.POST["Password"], request.POST["Email"], request.POST["NobreDeLaEmpresa"], request.POST["Celular"], request.POST["EmailEmp"])
            llenador.llenadorTablasEmpleadores(ob,[request.POST["Telefono"]])
        else:
            mensaje="Debes repetir el password"
    return render(request, "registerempresa.html", {'mensajePasswordInvalido':mensaje})

def recordsempleado(request):
    
    return render(request, "recordsempleado.html", {'tiempo': "re.tiempo", 'zona': "re.zona", 'exp': "re.exp", 'anterior': "re.anterior", 'descripcion': "re.descripcion"})


def homeempleador(request):
    
    return render(request, "homeempleador.html", {'tiempo':" he.tiempo",'nombre':"he.nombre", 'apellido':"he.apellido", 'zona':"he.zona",'exp':"he.exp",'anterior':"he.anterior",'descripcion':"he.descripcion"})



def descripcionempleado(request):
    
    return render(request, "descripcionempleado.html", {'tiempo': "de.tiempo",'nombre':"de.nombre", 'apellido':"de.apellido", 'zona':"de.zona",'exp':"de.exp", 'anterior':"de.anterior", 'descripcion':"de.descripcion"})



def forgotpassword(request):
    
    return render(request, "forgotpassword.html", {'password': "contraseña" })


def e404(request):
    return render(request, "404.html", {'llaveALaVerga6': "ValorALaVerga6"})

def homeempleado(request):
    
    return render(request, "homeempleado.html", {'tiempo': "tiempo",'nombre':"nombre", 'apellido':"apellido", 'zona':"zona",'exp':"exp",'anterior':"anterior",'descripcion':"descripcion"})