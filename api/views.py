# api/views.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Usuario, ServicioMunicipal, Evento, Alerta, PagoServicio, Comunicado, ContactoEmergencia, Barrio, TipoBasura, Basura
from .serializer import UsuarioSerializer, ServicioMunicipalSerializer, EventoSerializer, AlertaSerializer, PagoServicioSerializer, ComunicadoSerializer, ContactoEmergenciaSerializer, BarrioSerializer, TipoBasuraSerializer, BasuraSerializer

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer  # Permitir acceso a todos
    permission_classes = [AllowAny]

class ServicioMunicipalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServicioMunicipal.objects.all()
    serializer_class = ServicioMunicipalSerializer
    permission_classes = [AllowAny]

class EventoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [AllowAny]

class AlertaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer
    permission_classes = [AllowAny]

class PagoServicioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PagoServicio.objects.all()
    serializer_class = PagoServicioSerializer
    permission_classes = [AllowAny]

class ComunicadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comunicado.objects.all()
    serializer_class = ComunicadoSerializer
    permission_classes = [AllowAny]

class ContactoEmergenciaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactoEmergencia.objects.all()
    serializer_class = ContactoEmergenciaSerializer
    permission_classes = [AllowAny]

class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [AllowAny]

class TipoBasuraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoBasura.objects.all()
    serializer_class = TipoBasuraSerializer
    permission_classes = [AllowAny]

class BasuraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Basura.objects.all()
    serializer_class = BasuraSerializer
    permission_classes = [AllowAny]