from django.db import models
from datetime import date

# Create your models here.

#--------------Tabla Empleados-----------------#

class Empleados(models.Model):
    nombre=models.CharField( max_length = 80)
    codigo=models.CharField( max_length = 120)
    fechaNac=models.DateField()
    genero=models.CharField(max_length = 60)
    email=models.EmailField()

    def returnId(self):
        return self.id

class EmailRefetenceiaEmpleados(models.Model):
    llaveForanea=models.ForeignKey(Empleados,on_delete=models.CASCADE,)
    email=models.EmailField()

    def returnId(self):
        return self.id

class TelefonosEmpleados(models.Model):
    llaveForanea=models.ForeignKey(Empleados,on_delete=models.CASCADE,)
    telf=models.CharField(max_length = 8)

    def returnId(self):
        return self.id

#-----------------------------------------------#


#-----------Tabla Empleadores/Empresas----------#
class Empleadores(models.Model):
    nombre=models.CharField(max_length = 80)
    codigo= models.CharField(max_length = 80)
    email = models.EmailField()

class DireccionEmpleadores(models.Model):
    llaveForanea=models.ForeignKey(Empleadores,on_delete=models.CASCADE,)
    direccion=models.CharField(max_length = 200)

class TelefonosEmpleadores(models.Model):
    llaveForanea=models.ForeignKey(Empleadores,on_delete=models.CASCADE,)
    telf=models.CharField(max_length = 8)

#---------------------------------------------#

#-----------Tabla Tarjeta de trabajo-----------------#

class TarjetaTrabajo(models.Model):
    llaveForanea= models.ForeignKey(Empleados ,on_delete=models.CASCADE,)
    tiempoDisponoble=models.IntegerField()
    zona= models.CharField(max_length = 200)

class TagBusqueda(models.Model):
    llaveForanea=models.ForeignKey(TarjetaTrabajo, on_delete=models.CASCADE,)
    tag=models.CharField(max_length=30)

#-----------------------------------------------------_#

#--------------Relacion------------------------------#

class historialCreacion(models.Model):
    llaveForaneaTarjeta=models.ForeignKey(TarjetaTrabajo  , on_delete=models.CASCADE,)
    fechaCreacion=models.DateTimeField(default=date.today)
    llaveForaneaEmpleados=models.ForeignKey(Empleados  , on_delete=models.CASCADE,)

class historialConsulta(models.Model):
    llaveForaneaTarjeta=models.ForeignKey(TarjetaTrabajo  , on_delete=models.CASCADE,)
    fechaConsulta=models.DateTimeField(default=date.today)
    llaveForaneaEmpleadores=models.ForeignKey(Empleadores  ,on_delete=models.CASCADE,)
 #===================================================#