from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

class Persona:
	
	def __init__(self,usuario,contraseña):
		self.usuario = usuario
		self.contraseña = contraseña

def login(request):
    p1 = Persona("","")
    return render(request, "login.html", {'usuario': p1.usuario, 'contraseña': p1.contraseña})

class Empleado:
	
	def __init__(self,nombre,apellido,contraseña,contraseña2,email,celular,genero,fecha,usuario):
		self.nombre = nombre
		self.apellido = apellido
		self.contraseña = contraseña
		self.contraseña2 = contraseña2
		self.email = email
		self.celular = celular
		self.genero = genero
		self.fecha = fecha
		self.usuario = usuario

def registerempleado(request):
	e1 = Empleado("","","","","","","","","")
	return render(request, "registerempleado.html", {'nombreEmpleado': e1.nombre, 'apellidoEmpleado': e1.apellido, 'contraseña':e1.contraseña,'contraseña2':e1.contraseña2,'email':e1.email,'celular':e1.celular,'genero':e1.genero,'fecha':e1.fecha,'usuario':e1.usuario})

class Empresa:
	def __init__(self,usuarioE,contraseñaE,contraseñaE2,emailE,nombreEmpresa,celularE,telefono,emailDeLaEmpresa):
		self.usuarioE = usuarioE
		self.contraseñaE = contraseñaE
		self.contraseñaE2 = contraseñaE2
		self.emailE = emailE
		self.nombreEmpresa = nombreEmpresa
		self.celularE = celularE
		self.telefono = telefono
		self.emailDeLaEmpresa = emailDeLaEmpresa

def registerempresa(request):
    em=Empresa("","","","","","","","")
    return render(request, "registerempresa.html", {'usuarioE': em.usuarioE, 'contraseñaE': em.contraseñaE,'contraseñaE2':em.contraseñaE2,'emailE':em.emailE, 'nombreEmpresa':em.nombreEmpresa, 'celularE':em.celularE,'telefono':em.telefono,'emailDeLaEmpresa':em.emailDeLaEmpresa})

class Records:
	def __init__(self,tiempo,zona,exp,anterior,descripcion):
		#Empleado.__init__(self,nombre,apellido)
		self.tiempo = tiempo
		self.zona  = zona
		self.exp  = exp
		self.anterior = anterior
		self.descripcion  = descripcion

def recordsempleado(request):
	re = Records("","","","","")
    return render(request, "recordsempleado.html", {'tiempo': re.tiempo, 'zona': re.zona, 'exp': re.exp, 'anterior': re.anterior, 'descripcion': re.descripcion})

class homeEmpleador(Records):
	def __init__(self):
		Records.__init__(self,tiempo,zona,exp,anterior,descripcion)

def homeempleador(request):
    #he=homeEmpleador("","","","","")
    return render(request, "homeempleador.html", {'tiempo': tiempo,'nombre':nombre, 'apellido':apellido, 'zona':zona,'exp':exp,'anterior':anterior,'descripcion':descripcion})

class descpricionEmpleado(Records):
	def __init__(self):
		Records.__init__(self,tiempo,zona,exp,anterior,descripcion)

def descripcionempleado(request):
	#de=descpricionEmpleado("","","","","")
    return render(request, "descripcionempleado.html", {'tiempo': tiempo,'nombre':nombre, 'apellido':apellido, 'zona':zona,'exp':exp, 'anterior':anterior, 'descripcion':descripcion})

class olvidoLaCOntraseña(Persona):
	def __init__(self):
		Persona.__init__(self,contraseña)

def forgotpassword(request):
    fp = olvidoLaCOntraseña("")
    return render(request, "forgotpassword.html", {'password': contraseña})


def e404(request):
    return render(request, "404.html", {'llaveALaVerga6': "ValorALaVerga6"})

class homeEMpleado(Empleado):
	def __init__(self):
		Empleado.__init__(self,tiempo,zona,exp,anterior,descripcion)

def homeempleado(request):
	#hE = homeEMpleado("","","","","")
    return render(request, "homeempleado.html", {'tiempo': tiempo,'nombre':nombre, 'apellido':apellido, 'zona':zona,'exp':exp,'anterior':anterior,'descripcion':descripcion})
