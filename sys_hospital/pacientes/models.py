from django.db import models
from enderecos.models import Endereco

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE) # Ligação com o endereço

    def __str__(self):
        return self.nome