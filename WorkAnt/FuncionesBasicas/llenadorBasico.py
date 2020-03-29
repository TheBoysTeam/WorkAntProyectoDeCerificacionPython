from FuncionesBasicas.models import DireccionEmpleadores, EmailRefetenceiaEmpleados, Empleadores, Empleados, TagBusqueda, TarjetaTrabajo, TelefonosEmpleadores, TelefonosEmpleados, historialConsulta, historialCreacion


class llenadorTablas(self):

    def llenadorTablasUsuario(self, pnombre, pcodigo, pfechaNac, pgenero, email, emailReferencia, ptelefonosEmpleados):
        empleado = Empleados(nombre=pnombre, codigo=pcodigo,
                             fechaNac=pfechaNac, genero=pgenero)
        empleado.save()

        for i in emailReferencia:
            emailsR = EmailRefetenceiaEmpleados(
                llaveForanea=empleado, email=emailReferencia[i])
            email.save()

        for i in ptelefonosEmpleados:
            telfE = TelefonosEmpleados(
                llaveForanea=empleado, telf=ptelefonosEmpleados)
            telfE.save()

    def llenadorTablasEmpleadores(self, pnombre, pcodigo, pemail, pdireccionEmpleadores, ptelefonosEmpleadores):
        empleador = Empleadores(nombre=pnombre, codigo=pcodigo, emial=pemail)
        empleador.save()

        for i in pdireccionEmpleadores:
            direc = DireccionEmpleadores(
                llaveForanea=empleador, direccion=pdireccionEmpleadores[i])
            direc.save()

        for i in ptelefonosEmpleadores:
            telfE = TelefonosEmpleadores(
                llaveForanea=empleador, telf=ptelefonosEmpleadores[i])
            telfE.save()

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
