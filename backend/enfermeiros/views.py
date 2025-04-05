from rest_framework import viewsets, permissions
from .models import Enfermeiro
from .serializers import EnfermeiroSerializer

class EnfermeiroViewSet (viewsets.ModelViewSet):
    queryset = Enfermeiro.objects.all()
    serializer_class = EnfermeiroSerializer
    permission_classes = [permissions.AllowAny]