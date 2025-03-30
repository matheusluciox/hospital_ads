from rest_framework import serializers
from .models import statusConsulta

class statusConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = statusConsulta
        fields = '__all__'
