from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from FuncionesBasicas.models import Empleados, Empleadores
from FuncionesBasicas.llenadorBasico import llenadorTablasUsuario, llenadorTablasEmpleadores
import datetime


def login(request):
     return render(request, "login.html", {'usuario': "", 'contraseña': ""})

#------------------------------------------
def registerempleado(request):

    return render(request, "registerempleado.html", {"error":"todo ok"})

#------------------------------------------------------------------------------------------------------

#-----------------------------------------
def registerempresa(request):
    mensaje=""
    return render(request, "registerempresa.html", {'mensajePasswordInvalido':mensaje})
#--------------------------------------------------------------------------#
def recordsempleado(request):
    if request.POST["UsernameCreate"]:
        if request.POST["UsernameCreate"] and request.POST["Password"] and request.POST["RepeatPassword"] and request.POST["Email"] and request.POST["FechaNac"] and request.POST["Celular"] and request.POST["Genero"]:
            if not Empleados.objects.filter(nombre=request.POST["UsernameCreate"]).exists():
                if ( request.POST.get("Password",False) == request.POST.get("RepeatPassword",False) ):
                    #fecha=datetime.datetime.strptime(request.POST["FechaNac"], "%d%m%Y")
                    empleado=llenadorTablasUsuario(request.POST["UsernameCreate"],request.POST["Password"],request.POST["Genero"],request.POST["Email"])
                else:
                        return render(request, "registerempleado.html", {"error":"Repite el password"})
            else:
                return render(request, "registerempleado.html", {"error":"Ya existe ese usuario"})

    return render(request, "recordsempleado.html", {'tiempo': "re.tiempo", 'zona': "re.zona", 'exp': "re.exp", 'anterior': "re.anterior", 'descripcion': "re.descripcion"})

#------------------------------------------------------------------------------------#

def homeempleador(request):
    if request.POST["usuariologin"]:
        if request.POST["usuariologin"] and request.POST["contrasena"]:
            if Empleadores.objects.filter(nombre=request.POST["usuariologin"]).filter(codigo=request.POST["contrasena"]).exists():
                empleador=Empleadores.objects.filter(nombre=request.POST["usuariologin"]).filter(codigo=request.POST["contrasena"])
            else:
                return render(request, "login.html", {'error': "No existe el usuario o su codigo"})
        else:
            return render(request, "login.html", {'error': "No lleno todos los espacios necesarios"})
#------------------------------------------------------------------------------------------------#
    if request.POST["UsernameCreate"]:
        if request.POST["UsernameCreate"] and request.POST["Password"] and request.POST["RepeatPassword"] and request.POST["Email"] and request.POST["Celular"] and request.POST["Telefono"] and request.POST["EmailEmp"] :
            if not Empleados.objects.filter(nombre=request.POST["UsernameCreate"]).exists():
                if ( request.POST.get("Password",False) == request.POST.get("RepeatPassword",False) ):
                    
                    empleador=llenadorTablasEmpleadores(request.POST["UsernameCreate"],request.POST["Password"],request.POST["Email"] , request.POST["Celular"] , request.POST["EmailEmp"] )
                else:
                    return render(request, "registerempresa.html", {'mensajePasswordInvalido':"lol"})
            else:
                return render(request, "registerempresa.html", {'mensajePasswordInvalido':"lel"})
    
    return render(request, "homeempleador.html", {'tiempo':" he.tiempo",'nombre':"he.nombre", 'apellido':"he.apellido", 'zona':"he.zona",'exp':"he.exp",'anterior':"he.anterior",'descripcion':"he.descripcion"})

#--------------------------------------------------------------------------------------#

def descripcionempleado(request):
    
    return render(request, "descripcionempleado.html", {'tiempo': "de.tiempo",'nombre':"de.nombre", 'apellido':"de.apellido", 'zona':"de.zona",'exp':"de.exp", 'anterior':"de.anterior", 'descripcion':"de.descripcion"})



def forgotpassword(request):
    
    return render(request, "forgotpassword.html", {'password': "contraseña" })


def e404(request):
    return render(request, "404.html", {'llaveALaVerga6': "ValorALaVerga6"})

def loginEm(request):
    return render(request, "loginempresa.html", {"mm":"mm"})

def homeempleado(request):

    if request.POST["usuariologin"]:
        if request.POST["usuariologin"] and request.POST["contrasena"]:
            if Empleados.objects.filter(nombre=request.POST["usuariologin"]).filter(codigo=request.POST["contrasena"]).exists():
                empleados=Empleados.objects.filter(nombre=request.POST["usuariologin"]).filter(codigo=request.POST["contrasena"])
            else:
                return render(request, "login.html", {'error': "No existe el usuario o su codigo"})
        else:
            return render(request, "login.html", {'error': "No lleno todos los espacios necesarios"})
    
    return render(request, "homeempleado.html", {'tiempo': "tiempo",'nombre':"nombre", 'apellido':"apellido", 'zona':"zona",'exp':"exp",'anterior':"anterior",'descripcion':"descripcion"})