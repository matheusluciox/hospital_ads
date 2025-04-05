from rest_framework import serializers
from .models import Consultas

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = '__all__'