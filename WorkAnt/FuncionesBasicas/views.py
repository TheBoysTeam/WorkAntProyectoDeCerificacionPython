from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

class Persona:
	
	def __init__(self,usuario,contrasena):
		self.usuario = usuario
		self.contrasena = contrasena

def login(request):
    p1 = Persona("","")
    return render(request, "login.html", {'usuario': p1.usuario, 'contrasena': p1.contrasena})

class Empleado:
	
	def __init__(self,nombre,apellido,contrasena,contrasena2,email,celular,genero,fecha,usuario):
		self.nombre = nombre
		self.apellido = apellido
		self.contrasena = contrasena
		self.contrasena2 = contrasena2
		self.email = email
		self.celular = celular
		self.genero = genero
		self.fecha = fecha
		self.usuario = usuario

def registerempleado(request):
	e1 = Empleado("","","","","","","","","")
	return render(request, "registerempleado.html", {'nombreEmpleado': e1.nombre, 'apellidoEmpleado': e1.apellido, 'contrasena':e1.contrasena,'contrasena2':e1.contrasena2,'email':e1.email,'celular':e1.celular,'genero':e1.genero,'fecha':e1.fecha,'usuario':e1.usuario})

class Empresa:
	def __init__(self,usuarioE,contrasenaE,contrasenaE2,emailE,nombreEmpresa,celularE,telefono,emailDeLaEmpresa):
		self.usuarioE = usuarioE
		self.contrasenaE = contrasenaE
		self.contrasenaE2 = contrasenaE2
		self.emailE = emailE
		self.nombreEmpresa = nombreEmpresa
		self.celularE = celularE
		self.telefono = telefono
		self.emailDeLaEmpresa = emailDeLaEmpresa

def registerempresa(request):
    em=Empresa("","","","","","","","")
    return render(request, "registerempresa.html", {'usuarioE': em.usuarioE, 'contrasenaE': em.contrasenaE,'contrasenaE2':em.contrasenaE2,'emailE':em.emailE, 'nombreEmpresa':em.nombreEmpresa, 'celularE':em.celularE,'telefono':em.telefono,'emailDeLaEmpresa':em.emailDeLaEmpresa})

class Records:
	def __init__(self,nombreEmpleado):
		self.nombreEmpleado = nombreEmpleado
		#,apellido,tiempo,zona,exp,anterior,descripcion
		#self.apellido = apellido
		#self.tiempo = tiempo
		#self.zona = zona
		#self.exp = exp
		#self.anterior = anterior
		#self.descripcion = descripcion
		#,"","","","","",""

def recordsempleado(request):
	#re=Records("")
    return render(request, "recordsempleado.html", {'nombreEmpleado': re.nombreEmpleado})

class homeEmpleador:
	def __init__(self,nombre,apellido,tiempo,zona,exp,anterior,descripcion):
		#Records.__init__(self,tiempo,zona,exp,anterior,descripcion)
		self.nombre=nombre
		self.apellido=apellido
		self.anterior=anterior
		self.descripcion=descripcion
		self.zona=zona
		self.exp=exp
		self.tiempo=tiempo

def homeempleador(request):
    he=homeEmpleador("","","","","","","")
    return render(request, "homeempleador.html", {'tiempo': he.tiempo,'nombre':he.nombre, 'apellido':he.apellido, 'zona':he.zona,'exp':he.exp,'anterior':he.anterior,'descripcion':he.descripcion})

class descpricionEmpleado(Records):
	def __init__(self):
		Records.__init__(self,tiempo,zona,exp,anterior,descripcion)

def descripcionempleado(request):
	#de=descpricionEmpleado("","","","","")
    return render(request, "descripcionempleado.html", {'tiempo': tiempo,'nombre':nombre, 'apellido':apellido, 'zona':zona,'exp':exp, 'anterior':anterior, 'descripcion':descripcion})

class olvidoLaCOntrasena(Persona):
	def __init__(self):
		Persona.__init__(self,contrasena)

def forgotpassword(request):
    fp = olvidoLaCOntrasena("")
    return render(request, "forgotpassword.html", {'password': contrasena})


def e404(request):
    return render(request, "404.html", {'llaveALaVerga6': "ValorALaVerga6"})

class homeEMpleado(Empleado):
	def __init__(self):
		Empleado.__init__(self,tiempo,zona,exp,anterior,descripcion)

def homeempleado(request):
	#hE = homeEMpleado("","","","","")
    return render(request, "homeempleado.html", {'tiempo': tiempo,'nombre':nombre, 'apellido':apellido, 'zona':zona,'exp':exp,'anterior':anterior,'descripcion':descripcion})
