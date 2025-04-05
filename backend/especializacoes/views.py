from rest_framework import viewsets, permissions
from .models import Especializacao
from .serializers import EspecializacaoSerializer

class EspecializacaoViewSet (viewsets.ModelViewSet):
    queryset = Especializacao.objects.all()
    serializer_class = EspecializacaoSerializer
    permission_classes = [permissions.AllowAny]