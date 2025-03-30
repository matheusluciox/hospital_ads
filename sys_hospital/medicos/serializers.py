from rest_framework import serializers
from .models import Medico
from enderecos.serializers import EnderecoSerializer
from especializacoes.serializers import EspecializacaoSerializer

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'
