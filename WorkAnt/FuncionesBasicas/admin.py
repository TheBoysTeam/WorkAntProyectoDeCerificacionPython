from django.contrib import admin

from FuncionesBasicas.models import DireccionEmpleadores, EmailRefetenceiaEmpleados, Empleadores, Empleados, TagBusqueda, TarjetaTrabajo, TelefonosEmpleadores, TelefonosEmpleados, historialConsulta, historialCreacion

#--------------------------------------------------------------------------------------#

class EmpleadosAdmin(admin.ModelAdmin):
    list_display=("id","nombre","codigo","fechaNac","genero","email",)
    search_fields=("id","nombre","email")
    list_filter=("nombre",)

class EmpleadoresAdmin(admin.ModelAdmin):
    list_display=("id","nombre","codigo","email",)
    search_fields=("id","nombre","email")
    list_filter=("nombre",)

class TarjetasAdmin(admin.ModelAdmin):
    list_display=("id","llaveForanea","tiempoDisponible","zona")
    search_fields=("id","llaveForanea","tiempoDisponible","zona")
    list_filter=("llaveForanea",)

class HistorialCreacionAdmin(admin.ModelAdmin):
    list_display=("id","llaveForaneaTarjeta","fechaCreacion","llaveForaneaEmpleados")
    search_fields=("id", "llaveForaneTarjetas","llaveForaneaEmpleados")
    date_hierachy="fechaCreacion"

class HistorialConsultaAdmin(admin.ModelAdmin):
    list_display=("id","llaveForaneaTarjeta","fechaConsulta","llaveForaneaEmpleadores")
    search_fields=("id", "llaveForaneTarjetas","llaveForaneaEmpleadores")
    date_hierachy="fechaConsulta"

#--------------------------------------------------------------------------------------#



admin.site.register(Empleados,EmpleadosAdmin)
admin.site.register(Empleadores,EmpleadoresAdmin)
admin.site.register(TarjetaTrabajo,TarjetasAdmin)
admin.site.register(historialCreacion,HistorialCreacionAdmin)
admin.site.register(historialConsulta,HistorialConsultaAdmin)

