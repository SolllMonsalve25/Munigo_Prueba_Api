# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ServicioMunicipalViewSet, EventoViewSet, AlertaViewSet, PagoServicioViewSet, ComunicadoViewSet, ContactoEmergenciaViewSet, BarrioViewSet, TipoBasuraViewSet, BasuraViewSet

router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'servicios-municipal', ServicioMunicipalViewSet)
router.register(r'evento', EventoViewSet)
router.register(r'alerta', AlertaViewSet)
router.register(r'pago-servicio', PagoServicioViewSet)
router.register(r'comunicado', ComunicadoViewSet)
router.register(r'contacto-emergencia', ContactoEmergenciaViewSet)
router.register(r'barrio', BarrioViewSet)
router.register(r'tipos-basura', TipoBasuraViewSet)
router.register(r'basura', BasuraViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),  # Asegúrate de incluir esta línea
]