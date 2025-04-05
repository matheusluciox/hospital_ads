from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Consultas
from .serializers import ConsultaSerializer

class ConsultaViewSet (viewsets.ModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [permissions.AllowAny]