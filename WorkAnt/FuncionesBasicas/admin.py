from django.contrib import admin

from FuncionesBasicas.models import DireccionEmpleadores, EmailRefetenceiaEmpleados , Empleadores , Empleados , TagBusqueda, TarjetaTrabajo , TelefonosEmpleadores , TelefonosEmpleados ,TiempoDisponible ,ZonaTrabajo, historialConsulta , historialCreacion 

admin.site.register(DireccionEmpleadores)
admin.site.register(EmailRefetenceiaEmpleados)
admin.site.register(Empleadores)
admin.site.register(Empleados)
admin.site.register(TagBusqueda)
admin.site.register(TarjetaTrabajo)
admin.site.register(TelefonosEmpleadores)
admin.site.register(TelefonosEmpleados)
admin.site.register(TiempoDisponible)
admin.site.register(ZonaTrabajo)
admin.site.register(historialConsulta)
admin.site.register(historialCreacion)