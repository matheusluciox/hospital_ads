from rest_framework import viewsets, permissions
from .models import Medico
from .serializers import MedicoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [permissions.AllowAny]  # Permite qualquer acesso (para testes)