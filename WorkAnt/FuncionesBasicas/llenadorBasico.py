from FuncionesBasicas.models import DireccionEmpleadores, EmailRefetenceiaEmpleados, Empleadores, Empleados, TagBusqueda, TarjetaTrabajo, TelefonosEmpleadores, TelefonosEmpleados, historialConsulta, historialCreacion



def llenadorTablasUsuario(pnombre, pcodigo, pgenero, pemail):
        empleado = Empleados.objects.create(nombre=pnombre, codigo=pcodigo,genero=pgenero, email=pemail)
        return empleado

def llenadorTablasEmpleadores( pnombre, pcodigo, pemail,  celu , emailEmpre):
        empleador = Empleadores(nombre=pnombre, codigo=pcodigo, email=pemail, celular=celu, emailEmpresa =emailEmpre)
        empleador.save()
        return empleador
    
def telefonosEmpleados(ptelefonosEmpleados , empleado):
         for i in ptelefonosEmpleados:
            telfE = TelefonosEmpleados(llaveForanea=empleado, telf=ptelefonosEmpleados)
            telfE.save()


def direccionEmpleadores(self, pdireccionEmpleadores, empleador):
        l = []
        for i in pdireccionEmpleadores:
            direc = DireccionEmpleadores( llaveForanea=empleador, direccion=pdireccionEmpleadores[i]) 
            direc.save()
            l.append(direc)
        return l

class llenadorTablas:

    def llenadorTablasUsuario(self, pnombre, pcodigo, pgenero, pemail):
        empleado = Empleados.objects.create(nombre=pnombre, codigo=pcodigo,genero=pgenero, email=pemail)
        return empleado

    def emailReferencia(self,emailReferencia,empleado):
        l=[]
        for i in emailReferencia:
            emailsR = EmailRefetenceiaEmpleados( llaveForanea=empleado, email=emailReferencia[i])
            emailsR.save()
            l.append(emailsR)
        return l
        

    def telefonosEmpleados(self,  ptelefonosEmpleados , empleado):
         for i in ptelefonosEmpleados:
            telfE = TelefonosEmpleados(llaveForanea=empleado, telf=ptelefonosEmpleados)
            telfE.save()

    def llenadorTablasEmpleadores(self, pnombre, pcodigo, pemail,  celu , emailEmpre, telf):
        empleador = Empleadores(nombre=pnombre, codigo=pcodigo, emial=pemail, celular=celu, emailEmpresa =emailEmpre)
        empleador.save()
        return empleador

    def direccionEmpleadores(self, pdireccionEmpleadores, empleador):
        l = []
        for i in pdireccionEmpleadores:
            direc = DireccionEmpleadores( llaveForanea=empleador, direccion=pdireccionEmpleadores[i]) 
            direc.save()
            l.append(direc)
        return l

    def telefonosEmpleadores(self,  ptelefonosEmpleadores, empleador ):
        l = []
        for i in ptelefonosEmpleadores:
            telfE = TelefonosEmpleadores(llaveForanea=empleador, telf=ptelefonosEmpleadores[i])
            telfE.save()
            l.append(telfE)
        return l


    def llenadorTablasTarjetas(self, empleado_id, ptimempoDisponible,  pzona, ptagBusqueda):
        empleado = Empleados.objects.get(id=empleado_id)

        tarjeta = TarjetaTrabajo(
            llaveForanea=empleado, tiempoDisponible=ptimempoDisponible, zona=pzona)
        tarjeta.save()

        for i in ptagBusqueda:
            ttag = TagBusqueda(llaveForanea=tarjeta, tag=ptagBusqueda[i])
            ttag.save()


    def llenadorTablasHistorialCreacion(self, tarjeta_id, empleado_id):
        tarjeta = TarjetaTrabajo.objects.get(id=tarjeta_id)
        empleado = Empleados.objects.get(id=empleado_id)

        hcreacion = historialCreacion(
            llaveForaneaTarjeta=tarjeta, llaveForaneaEmpleados=empleado)
        hcreacion.save()


    def llenadorTablasHistorialConsulta(self, tarjeta_id, empleador_id):
        tarjeta = TarjetaTrabajo.objects.get(id=tarjeta_id)
        empleador = Empleadores.objects.get(id=empleador_id)

        hcreacion = historialConsulta(
            llaveForaneaTarjeta=tarjeta, llaveForaneaEmpleadores=empleador)
        hcreacion.save()
