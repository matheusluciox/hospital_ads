from rest_framework import viewsets, permissions
from .models import statusConsulta
from .serializers import statusConsultaSerializer

class statusConsultaViewSet(viewsets.ModelViewSet):
    queryset = statusConsulta.objects.all()
    serializer_class = statusConsultaSerializer
    permission_classes = [permissions.AllowAny]  # Permite qualquer acesso (para testes)