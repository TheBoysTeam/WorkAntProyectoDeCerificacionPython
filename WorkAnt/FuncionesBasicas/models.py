from django.db import models
from datetime import date


#--------------Tabla Empleados-----------------#


class Empleados(models.Model):
    nombre = models.CharField(max_length=80, unique = True)
    codigo = models.CharField(max_length=120)
    fechaNac = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=60)
    email = models.EmailField()



class EmailRefetenceiaEmpleados(models.Model):

    llaveForanea=models.ForeignKey(Empleados,on_delete=models.CASCADE,default=0)
    email=models.EmailField()




class TelefonosEmpleados(models.Model):

    llaveForanea=models.ForeignKey(Empleados,on_delete=models.CASCADE,default=0)
    telf=models.CharField(max_length = 8)


#-----------------------------------------------#


#-----------Tabla Empleadores/Empresas----------#
class Empleadores(models.Model):
    nombre = models.CharField(max_length=80, unique = True)
    codigo = models.CharField(max_length=80)
    email = models.EmailField()
    celular=models.CharField(max_length=8)
    emailEmpresa= models.CharField(max_length=80)

class DireccionEmpleadores(models.Model):
    llaveForanea=models.ForeignKey(Empleadores,on_delete=models.CASCADE,default=0)
    direccion=models.CharField(max_length = 200)

class TelefonosEmpleadores(models.Model):
    llaveForanea=models.ForeignKey(Empleadores,on_delete=models.CASCADE,default=0)
    telf=models.CharField(max_length = 8)

#---------------------------------------------#

#-----------Tabla Tarjeta de trabajo-----------------#


class TarjetaTrabajo(models.Model):

    llaveForanea= models.ForeignKey(Empleados ,on_delete=models.CASCADE, default=0)
    tiempoDisponible=models.IntegerField()
    zona= models.CharField(max_length = 200)

class TagBusqueda(models.Model):
    llaveForanea=models.ForeignKey(TarjetaTrabajo, on_delete=models.CASCADE,default=0)
    tag=models.CharField(max_length=30)


#-----------------------------------------------------_#

#--------------Relacion------------------------------#


class historialCreacion(models.Model):

    llaveForaneaTarjeta=models.ForeignKey(TarjetaTrabajo  , on_delete=models.CASCADE, default=0)
    fechaCreacion=models.DateTimeField(default=date.today)
    llaveForaneaEmpleados=models.ForeignKey(Empleados  , on_delete=models.CASCADE,default=0)

class historialConsulta(models.Model):
    llaveForaneaTarjeta=models.ForeignKey(TarjetaTrabajo  , on_delete=models.CASCADE,default=0)
    fechaConsulta=models.DateTimeField(default=date.today)
    llaveForaneaEmpleadores=models.ForeignKey(Empleadores  ,on_delete=models.CASCADE,default=0)
 #===================================================#

