from django.contrib import admin
from .models import Usuario, ServicioMunicipal, Evento, Alerta, PagoServicio, Comunicado, ContactoEmergencia, Barrio, TipoBasura, Basura

admin.site.register(Usuario)
admin.site.register(ServicioMunicipal)
admin.site.register(Evento)
admin.site.register(Alerta)
admin.site.register(PagoServicio)
admin.site.register(Comunicado)
admin.site.register(ContactoEmergencia)
admin.site.register(Barrio)
admin.site.register(TipoBasura)
admin.site.register(Basura)